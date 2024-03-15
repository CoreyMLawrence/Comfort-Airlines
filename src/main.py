# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Date: 2/19/2024
#
# Description:
#   This module is the entry point to the program. All pre-program initialization is performed
#   here before the simulation is started.
import itertools
import csv
from pprint import pprint

import structlog
from haversine import haversine

import log.processors
from singletons.simulation import Simulation
from constants import HUB_NAMES, SIMULATION_DURATION, DEFAULT_LANDING_FEE, DEFAULT_TAKEOFF_FEE, DEFAULT_GAS_PRICE
from models.aircraft import AircraftFactory, AircraftType, AircraftStatus
from models.airport import Airport
from models.route import Route

def import_hubs(filepath: str) -> list[Airport]:
    # rank,airport,iata code,city,state,metro area,metro population,latitude,longitude
    RANK = 0
    AIRPORT_NAME = 1
    IATA_CODE = 2
    CITY = 3
    STATE = 4
    METRO_AREA_NAME = 5
    METRO_AREA_POPULATION = 6
    LATITUDE = 7
    LONGITUDE = 8

    with open(filepath, "r") as data:
        reader = csv.reader(data, delimiter=",")
        _ = next(reader)
        hubs = []
        
        for row in reader:
            if row[AIRPORT_NAME] in HUB_NAMES:
                hubs.append(
                    Airport(
                        row[AIRPORT_NAME], row[IATA_CODE], row[CITY], row[STATE], 
                        float(row[LATITUDE]), float(row[LONGITUDE]), [], None, 
                        row[METRO_AREA_NAME], int(row[METRO_AREA_POPULATION]),
                        DEFAULT_GAS_PRICE, DEFAULT_TAKEOFF_FEE, DEFAULT_LANDING_FEE
                    )
                )
            
    return hubs
            

def import_airports(filepath: str, airports: list[Airport]) -> None:
    RANK = 0
    AIRPORT_NAME = 1
    IATA_CODE = 2
    CITY = 3
    STATE = 4
    METRO_AREA_NAME = 5
    METRO_AREA_POPULATION = 6
    LATITUDE = 7
    LONGITUDE = 8
    
    with open(filepath, "r") as data:
       reader = csv.reader(data, delimiter=",")
       _ = next(reader)
       for row in reader:
           if not row[AIRPORT_NAME] in HUB_NAMES:
               name = row[AIRPORT_NAME]
               iata_code = row[IATA_CODE]
               city = row[CITY]
               state = row[STATE]
               latitude = float(row[LATITUDE])
               longitude = float(row[LONGITUDE])
               routes = []
               metro_area = row[METRO_AREA_NAME]
               metro_population = int(row[METRO_AREA_POPULATION])
               
               closest_hub = airports[0]
               for i in range(len(HUB_NAMES)):
                   hub = airports[i]
                   
                   if haversine((latitude,longitude), (hub.latitude,hub.longitude)) < haversine((latitude,longitude),(closest_hub.latitude,closest_hub.longitude)):
                       closest_hub = hub
               
               airports.append(
                   Airport(
                       name, iata_code, city, state, latitude, longitude, routes, closest_hub,
                       metro_area, metro_population, DEFAULT_GAS_PRICE, DEFAULT_TAKEOFF_FEE, DEFAULT_LANDING_FEE
                   )
               ) 

def import_routes(filename: str) -> list[Route]:
    return []

def main() -> None:
    """The entry point for the application"""
    
    aircraft = list(itertools.chain.from_iterable([
        [AircraftFactory.create_aircraft(AircraftType.BOEING_737_600, AircraftStatus.AVAILABLE, None, 0) for _ in range(15)],
        [AircraftFactory.create_aircraft(AircraftType.BOEING_737_800, AircraftStatus.AVAILABLE, None, 0) for _ in range(15)],
        [AircraftFactory.create_aircraft(AircraftType.AIRBUS_A200_100, AircraftStatus.AVAILABLE, None, 0) for _ in range(12)],
        [AircraftFactory.create_aircraft(AircraftType.AIRBUS_A220_300, AircraftStatus.AVAILABLE, None, 0) for _ in range(13)]
    ]))
    
    # Import hubs
    # Import local airports
    # Import routes
    # Set routes for airports
    airports = import_hubs("./data/airports.csv")
    import_airports("./data/airports.csv", airports)
    routes = import_routes()

    #for airport in airports:
    #    airport.routes = list(filter(lambda route: route.source_airport == airport.name, routes))

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
    
    # simulation.run()

if __name__ == "__main__":
    main()