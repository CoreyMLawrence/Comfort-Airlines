from __future__ import annotations
from typing import TYPE_CHECKING
from decimal import Decimal
import csv
from pprint import pprint

import structlog

from constants import DEBUG, VERBOSE, AGGREGATE, HUB_NAMES, MINUTES_PER_DAY
from singletons.ledger import Ledger, LedgerEntry, LedgerEntryType
from models.aircraft import Aircraft, AircraftStatus, AircraftType, WAIT_TIMERS
from models.flight import Flight
from helpers.default import default
from helpers.first import first

if TYPE_CHECKING:
    from models.route import Route
    from models.passenger import Passenger
    from singletons.ledger import Ledger

class Scheduler:
    flight_uuid = 0
    flights: list[Flight] = []
    logger = structlog.get_logger()
    
    @staticmethod
    def __next_flight_uuid() -> int:
        id = Scheduler.flight_uuid
        Scheduler.flight_uuid += 1

        return id
    
    @staticmethod
    def __within_operating_hours(time: int) -> bool:
        ONE_AM = 60
        FIVE_AM = 300
        time %= MINUTES_PER_DAY
        return time < ONE_AM or time > FIVE_AM
        
    @staticmethod
    def schedule_flight(ledger: Ledger, time: int, aircraft: Aircraft, routes: list[Route], passengers: list[Passenger]):
        if aircraft.status != AircraftStatus.AVAILABLE:
            raise ValueError("Precondition failed: aircraft is not available for scheduling")

        compatible_routes = [route for route in routes if route.aircraft_type == aircraft.type and route.current_demand > 0]
        compatible_routes = [route for route in compatible_routes if Scheduler.__within_operating_hours(time + route.expected_time)]

        if aircraft.type == AircraftType.BOEING_747_400:
            if aircraft.needs_maintenance:
                compatible_routes = [
                    route for route in compatible_routes
                    if route.destination_airport.name in HUB_NAMES
                ]
            else:
                if aircraft.location.name == "John F. Kennedy International Airport":
                    compatible_routes = [
                        route for route in compatible_routes
                        if route.destination_airport.name == "Paris Charles de Gaulle Airport"
                    ]
                else:
                    compatible_routes = [
                        route for route in compatible_routes
                        if route.destination_airport.name == "John F. Kennedy International Airport"
                    ]

        compatible_routes = [
            route for route in compatible_routes if len([
                passenger for passenger in passengers 
                if passenger.location == route.source_airport and passenger.destination == route.destination_airport
            ]) > 0
        ]

        if aircraft.needs_maintenance:
            compatible_routes = [route for route in compatible_routes if route.destination_airport.is_hub]

        if len(compatible_routes) == 0:
            if DEBUG:
                Scheduler.logger.info("no flight could be scheduled", aircraft_tail_number=aircraft.tail_number)
            return

        route = max(compatible_routes, key=lambda route: route.net_profit)
        if AGGREGATE and not route.destination_airport.is_hub:
            route_to_regional_airport = first(lambda r: r.destination_airport == route.destination_airport.regional_airport, compatible_routes)
            if not route_to_regional_airport is None:
                route = route_to_regional_airport
        
        
        passengers = [
            passenger for passenger in passengers 
            if passenger.location == route.source_airport and passenger.destination == route.destination_airport
        ][:aircraft.passenger_capacity]
        route.daily_demand -= min(route.daily_demand, len(passengers))
        if VERBOSE:
            Scheduler.logger.debug("decreased route daily demand", route=str(route), current_demand=route.current_demand, daily_demand=route.daily_demand)

        if aircraft.fuel_level < route.fuel_requirement:
            ledger.record(LedgerEntry(LedgerEntryType.FUEL, -(Decimal((aircraft.fuel_capacity - aircraft.fuel_level)) * aircraft.location.gas_price), time, aircraft.location))
            aircraft.fuel_level = aircraft.fuel_capacity
            aircraft.set_status(AircraftStatus.BOARDING_WITH_REFUELING)
        else:
            aircraft.set_status(AircraftStatus.BOARDING_WITHOUT_REFUELING)
    
        expected_departure_time = time + (WAIT_TIMERS[AircraftStatus.BOARDING_WITH_REFUELING] if aircraft.status == AircraftStatus.BOARDING_WITH_REFUELING else WAIT_TIMERS[AircraftStatus.BOARDING_WITHOUT_REFUELING])
        expected_arrival_time = expected_departure_time + route.expected_time + WAIT_TIMERS[AircraftStatus.DEBOARDING]
    
        flight = Flight(
            Scheduler.__next_flight_uuid(),
            time,
            aircraft,
            route,
            passengers,
            expected_departure_time,
            expected_arrival_time
        )
        
        for passenger in passengers:
            passenger.location = None
            passenger.flights_taken.append(flight)
        
        Scheduler.logger.info("scheduled flight", aircraft_tail_number=aircraft.tail_number, source_airport=route.source_airport.name, destination_airport=route.destination_airport.name, aircraft_type=aircraft.type.name)
        
        aircraft.flight = flight
        aircraft.flights_taken.append(flight)
        Scheduler.flights.append(flight)