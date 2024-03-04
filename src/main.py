# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Date: 2/19/2024
#
# Description:
#   This module is the entry point to the program. All pre-program initialization is performed
#   here before the simulation is started.
from typing import TYPE_CHECKING
import itertools
import csv
from pprint import pprint

import structlog

import log.processors
from simulation import Simulation
from models.aircraft import AircraftFactory, AircraftType, AircraftStatus
from models.airport import Airport, DEFAULT_LANDING_FEE, DEFAULT_TAKEOFF_FEE, DEFAULT_GAS_PRICE
from models.route import Route

def import_airports(filepath: str) -> list[Airport]:
    DELIMITER = ","
    RANK = 0
    NAME = 1
    IATA_CODE = 2
    CITY = 3
    STATE =  4
    METRO_AREA = 5
    METRO_POPULATION = 6
    LATITUDE = 7
    LONGITUDE = 8
    
    airports = []
    
    with open(filepath, "r") as file:
        rows = csv.reader(file, delimiter=DELIMITER)
        _ = next(rows)
        
        for airport in rows:
            airports.append(
                Airport(
                    airport[NAME], airport[IATA_CODE], airport[CITY], airport[STATE], airport[LATITUDE], airport[LONGITUDE], [], [], None,
                    airport[METRO_AREA], int(airport[METRO_POPULATION]), DEFAULT_GAS_PRICE, DEFAULT_TAKEOFF_FEE, DEFAULT_LANDING_FEE
                )
            )
            
    return airports

def import_routes(filepath: str) -> list[Route]:
    DELIMITER=","
    FUEL_OFFSET = 4
    
    SOURCE_AIRPORT = 0
    DESTINATION_AIRPORT = 1
    DISTANCE = 2
    DEMAND = 3
    FUEL_REQUIRED_BOEING_737_600 = 4
    FUEL_REQUIRED_BOEING_737_800 = 5
    FUEL_REQUIRED_AIRBUS_A200_100 = 6
    FUEL_REQUIRED_AIRBUS_A220_300 = 7

    routes = []
    
    with open(filepath, "r") as file:
        rows = csv.reader(file, delimiter=DELIMITER)
        _ = next(rows)
        
        for route in rows:
            for aircraft_type in AircraftType:
                if float(route[int(aircraft_type) + FUEL_OFFSET]) != -1:
                    routes.append(
                        Route(
                            aircraft_type, route[SOURCE_AIRPORT], route[DESTINATION_AIRPORT], 
                            route[DISTANCE], route[int(aircraft_type) + FUEL_OFFSET]
                        )
                    )
            
    return routes

def main() -> None:
    """The entry point for the application"""
    MINUTES_PER_DAY = 1440
    SIMULATION_DURATION_DAYS = 14
    SIMULATION_DURATION = MINUTES_PER_DAY * SIMULATION_DURATION_DAYS
    
    aircraft = list(itertools.chain.from_iterable([
        [AircraftFactory.create_aircraft(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, 0) for _ in range(15)],
        [AircraftFactory.create_aircraft(AircraftType.BOEING_737_800, AircraftStatus.AVAILABLE, None, 0) for _ in range(15)],
        [AircraftFactory.create_aircraft(AircraftType.AIRBUS_A200_100, AircraftStatus.AVAILABLE, None, 0) for _ in range(12)],
        [AircraftFactory.create_aircraft(AircraftType.AIRBUS_A220_300, AircraftStatus.AVAILABLE, None, 0) for _ in range(13)]
    ]))
    airports = import_airports("./data/airports.csv")
    routes = import_routes("./data/flights.csv")
    
    for airport in airports:
        airport.routes = list(filter(lambda route: route.source_airport == airport.name, routes))
    
    for route in routes:
        route.source_airport = list(filter(lambda airport: airport.name == route.source_airport, airports))[0]
        route.destination_airport = list(filter(lambda airport: airport.name == route.destination_airport, airports))[0]
        pprint(f"{route.source_airport}, {route.source_airport.iata_code}")

    
    simulation = Simulation(SIMULATION_DURATION, aircraft, airports, routes)
    
    structlog.configure(
        processors=[
            log.processors.CodeLocation(),
            log.processors.ProcessorID(),
            log.processors.ProcessorSimulationTime(simulation.time),
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="%H:%M:%S", utc=True, key="real_time"),
            structlog.processors.JSONRenderer()
        ]
    )
    
    simulation.run()

if __name__ == "__main__":
    main()