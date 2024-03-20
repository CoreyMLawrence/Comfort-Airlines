from __future__ import annotations
from typing import TYPE_CHECKING
import itertools
import time as t
from pprint import pprint

import structlog
from haversine import haversine

from constants import HUB_NAMES, MINUTES_PER_DAY, DEBUG
from singletons.scheduler import Scheduler

from helpers.reference_wrapper import ReferenceWrapper

from models.passenger import Passenger
from models.aircraft import Aircraft, AircraftStatus

if TYPE_CHECKING:
    from models.airport import Airport
    from models.route import Route

class Simulation:
    def __init__(self, duration: int, aircrafts: list[Aircraft], airports: list[Airport], routes: list[Route]):
        self.duration = duration
        self.aircrafts = aircrafts
        self.airports = airports
        self.hubs = self.airports[:len(HUB_NAMES)]
        self.routes = routes
        self.passengers: list[Passenger] = []
        
        self.time = ReferenceWrapper(0)
        self.logger = structlog.get_logger()
        
    def spawn_passengers(self) -> None:
        self.passengers = list(filter(lambda passenger: passenger.location != passenger.source_airport, self.passengers))
        
        for route in self.routes:
            self.passengers.extend([Passenger(route.source_airport, route.destination_airport) for _ in range(route.demand)])
            
        if DEBUG:
            self.logger.info("spawned passengers", num_passengers=len(self.passengers))

    def run(self) -> None:
        while self.time.value < self.duration:
            if self.time.value % MINUTES_PER_DAY == 0:
                self.spawn_passengers()
                
            for aircraft in self.aircrafts:
                if aircraft.status == AircraftStatus.AVAILABLE:
                    if aircraft.needs_maintenance:
                        if aircraft.location.is_hub and aircraft.location.maintenance_gates > 0:
                            aircraft.location.maintenance_gates -= 1
                            aircraft.set_status(AircraftStatus.IN_MAINTENANCE)
                        else:
                            Scheduler.schedule_flight(self.time, aircraft, self.routes, self.passengers)
                    else:
                        Scheduler.schedule_flight(self.time, aircraft, self.routes, self.passengers)
                else:
                    if aircraft.status == AircraftStatus.IN_FLIGHT and aircraft.wait_timer <= 0:
                        aircraft.arrive(self.time)
                    if aircraft.status == AircraftStatus.IN_MAINTENANCE and aircraft.wait_timer <= 0:
                        aircraft.set_status(AircraftStatus.AVAILABLE)
                        aircraft.flight_hours = 0
                        
                        aircraft.location.assign_gate(aircraft)
                    
                    if aircraft.status in [AircraftStatus.BOARDING_WITHOUT_REFUELING, AircraftStatus.BOARDING_WITH_REFUELING] and aircraft.wait_timer <= 0:
                       aircraft.set_status(AircraftStatus.IN_FLIGHT)
                       aircraft.wait_timer = aircraft.flight.route.expected_time
                       aircraft.depart(self.time)

                    if aircraft.status == AircraftStatus.DEBOARDING and aircraft.wait_timer <= 0:
                        aircraft.set_status(AircraftStatus.AVAILABLE)
                        aircraft.flight.actual_arrival_time = self.time
                        for passenger in aircraft.flight.passengers:
                            passenger.location = aircraft.location
            
            for aircraft in self.aircrafts:
                if aircraft.wait_timer is not None:
                    aircraft.wait_timer -= 1
            self.time.value += 1