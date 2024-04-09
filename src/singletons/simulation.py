from __future__ import annotations
from typing import TYPE_CHECKING

import structlog

from constants import HUB_NAMES, MINUTES_PER_DAY, DEBUG, VERBOSE
from singletons.scheduler import Scheduler

from helpers.reference_wrapper import ReferenceWrapper
from helpers.decorators import timed

from models.passenger import Passenger
from models.aircraft import Aircraft, AircraftStatus

if TYPE_CHECKING:
    from models.airport import Airport
    from models.route import Route
    from singletons.ledger import Ledger
    from models.reports.passenger_report import PassengerReport
    from models.reports.airport_report import AirportReport
    from models.reports.aircraft_report import AircraftReport
    from models.reports.flight_report import FlightReport

class Simulation:
    def __init__(self, duration: int, ledger: Ledger, passenger_report: PassengerReport, airport_report: AirportReport, aircraft_report: AircraftReport, flight_report: FlightReport, aircrafts: list[Aircraft], airports: list[Airport], routes: list[Route]):
        self.duration = duration
        self.ledger = ledger
        self.aircrafts = aircrafts
        self.airports = airports
        self.hubs = self.airports[:len(HUB_NAMES)]
        self.routes = routes
        self.passengers: list[Passenger] = []
        
        self.time = ReferenceWrapper(0)
        self.logger = structlog.get_logger()
        self.passenger_report = passenger_report
        self.airport_report = airport_report
        self.aircraft_report = aircraft_report
        self.flight_report = flight_report
        
    def spawn_passengers(self) -> None:
        self.passengers = list(filter(lambda passenger: passenger.location != passenger.source_airport, self.passengers))
        
        for route in self.routes:
            self.passengers.extend([Passenger(route.source_airport, route.destination_airport) for _ in range(route.daily_demand)])
            
        if DEBUG:
            self.logger.info("spawned passengers", num_passengers=len(self.passengers))

    def daily_reset(self) -> None:
        if VERBOSE:
            self.logger.debug("before daily reset", num_passengers=len(self.passengers))
        
        for index, passenger in enumerate(self.passengers):
            if passenger.location == passenger.destination:
                self.passenger_report.log(passenger)
                self.passengers.pop(index)
                
        if VERBOSE:
            self.logger.debug("after daily purge", num_passengers=len(self.passengers))
        
        self.spawn_passengers()
        for route in self.routes:
            route.current_demand = route.daily_demand

        if VERBOSE:
            self.logger.debug("after daily reset", num_passengers=len(self.passengers))

    @timed
    def run(self) -> None:
        self.logger.info("started simulation")

        while self.time.value < self.duration:
            if self.time.value % MINUTES_PER_DAY == 0:
                self.daily_reset()
                
            for aircraft in self.aircrafts:
                if aircraft.status == AircraftStatus.AVAILABLE:
                    if aircraft.needs_maintenance:
                        if aircraft.location.is_hub and aircraft.location.maintenance_gates > 0:
                            aircraft.location.maintenance_gates -= 1
                            aircraft.set_status(AircraftStatus.IN_MAINTENANCE)
                        else:
                            Scheduler.schedule_flight(self.ledger, self.time.value, aircraft, aircraft.location.routes, self.passengers)
                    else:
                        Scheduler.schedule_flight(self.ledger, self.time.value, aircraft, aircraft.location.routes, self.passengers)
                else:
                    if aircraft.status == AircraftStatus.IN_FLIGHT and aircraft.wait_timer <= 0:
                        aircraft.arrive(self.ledger, aircraft.flight.route.destination_airport, self.time.value)

                    if aircraft.status == AircraftStatus.IN_MAINTENANCE and aircraft.wait_timer <= 0:
                        aircraft.set_status(AircraftStatus.AVAILABLE)
                        aircraft.flight_minutes = 0
                        aircraft.location.assign_gate(aircraft)

                        if len(aircraft.location.maintenance_queue) > 0:
                            queued_aircraft = aircraft.location.maintenance_queue.pop(0)
                            queued_aircraft.set_status(AircraftStatus.IN_MAINTENANCE)
                        else:
                            aircraft.location.maintenance_gates += 1

                    if aircraft.status in [AircraftStatus.BOARDING_WITHOUT_REFUELING, AircraftStatus.BOARDING_WITH_REFUELING] and aircraft.wait_timer <= 0:
                       aircraft.set_status(AircraftStatus.IN_FLIGHT)
                       aircraft.wait_timer = aircraft.flight.route.expected_time
                       aircraft.depart(self.ledger, self.time.value)

                    if aircraft.status == AircraftStatus.DEBOARDING and aircraft.wait_timer <= 0:
                        aircraft.set_status(AircraftStatus.AVAILABLE)
                        
                        if not aircraft.flight is None:
                            aircraft.flight.actual_arrival_time = self.time.value
                            for passenger in aircraft.flight.passengers:
                                passenger.location = aircraft.location
            
            for aircraft in self.aircrafts:
                if aircraft.wait_timer is not None:
                    aircraft.wait_timer -= 1
            self.time.value += 1

        self.logger.info("ended simulation")
        
        for aircraft in self.aircrafts:
            self.airport_report.log(aircraft)
            self.aircraft_report.log(aircraft)
            
            for flight in aircraft.flights_taken:
                self.flight_report.log(flight)
                
        for passenger in self.passengers:
            self.passenger_report.log(passenger)
        