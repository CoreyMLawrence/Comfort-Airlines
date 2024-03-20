from __future__ import annotations
from typing import TYPE_CHECKING
from decimal import Decimal

import structlog

from constants import DEBUG
from singletons.ledger import Ledger, LedgerEntry, LedgerEntryType
from models.aircraft import Aircraft, AircraftStatus, WAIT_TIMERS
from models.flight import Flight

if TYPE_CHECKING:
    from models.route import Route
    from models.passenger import Passenger

class Scheduler:
    flight_uuid = 0
    flights: list[Flight] = []
    logger = structlog.get_logger()
    
    @staticmethod
    def __next_flight_uuid() -> int:
        id = Scheduler.flight_uuid
        Scheduler.flight_uuid += 1

        return id
        
    def schedule_flight(time: int, aircraft: Aircraft, routes: list[Route], passengers: list[Passenger]):
        compatible_routes = filter(lambda route: route.source_airport == aircraft.location, routes)
        compatible_routes = filter(lambda route: route.aircraft_type == aircraft.type, compatible_routes)
        compatible_routes = filter(lambda route: route.fuel_requirement <= aircraft.fuel_capacity, compatible_routes)
        compatible_routes = filter(lambda route: len(list(filter(lambda passenger: passenger.location == route.source_airport and passenger.destination == route.destination_airport, passengers))) > 0, compatible_routes)
        
        if aircraft.needs_maintenance:
            compatible_routes = filter(lambda route: route.destination_airport.is_hub, compatible_routes)
            
        if not compatible_routes:
            if DEBUG:
                Scheduler.logger.info("no flight could be scheduled", aircraft_tail_number=aircraft.tail_number)
            return

        route = max(list(compatible_routes), key=lambda route: route.net_profit)
        passengers = list(filter(lambda passenger: passenger.location == route.source_airport and passenger.destination == route.destination_airport, passengers))
        
        if aircraft.fuel_level < route.fuel_requirement:
            Ledger.record(LedgerEntry(LedgerEntryType.FUEL, Decimal((aircraft.fuel_capacity - aircraft.fuel_level)) * aircraft.location.gas_price, time, aircraft.location))
            aircraft.fuel_level = aircraft.fuel_capacity
            aircraft.set_status(AircraftStatus.BOARDING_WITH_REFUELING)
        else:
            aircraft.set_status(AircraftStatus.BOARDING_WITHOUT_REFUELING)
    
        expected_departure_time = time + (WAIT_TIMERS[AircraftStatus.BOARDING_WITH_REFUELING] if aircraft.status == AircraftStatus.BOARDING_WITH_REFUELING else WAIT_TIMERS[AircraftStatus.BOARDING_WITHOUT_REFUELING])
        expected_arrival_time = expected_departure_time + route.expected_time + WAIT_TIMERS[AircraftStatus.DEBOARDING]
    
        # self, flight_number: int, time: int, aircraft: Aircraft, route: Route, passengers: list[Passenger], expected_departure_time: int, expected_arrival_time: int
        flight = Flight(
            Scheduler.__next_flight_uuid(),
            time,
            aircraft,
            route,
            passengers,
            expected_departure_time,
            expected_arrival_time
        )
        
        if DEBUG:
            Scheduler.logger.info("scheduled flight", aircraft_tail_number=aircraft.tail_number, source_airport=route.source_airport.name, destination_airport=route.destination_airport.name)
        
        aircraft.flight = flight
        Scheduler.flights.append(flight)

    def serialize(filepath: str) -> None:
        pass