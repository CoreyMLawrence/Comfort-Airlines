# Team: Foobar
# Authors: Anthony Cox, Dylan Hudson
# Date: 1/31/2024
# Script: flight_combine.py
# Depends on: "airports.csv", "flight_distance.csv", "flight_fuel_capacity.csv"
# Input: 
#   Lists of the source and destination airports and the distance between them and the flight demand for them
# Output: 
#   An aggregated list of the lists
import csv
from pprint import pprint

# Indices of values in flights.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DISTANCE_KM = 2

# Indices of values in flight_demand.csv
# SOURCE_AIRPORT = 0
# DESTINATION_AIRPORT = 1
NUM_PASSENGERS = 2

# Indices of values in flight_fuel_capacity.csv
# SOURCE_AIRPORT = 0
# DESTINATION_AIRPORT = 1

# Indices of values in aircraft.csv
AIRCRAFT = 0
PASSENGER_CAPACITY = 1
CRUISE_SPEED = 2
MAX_FUEL_CAPACITY = 3
MAX_RANGE = 4
MPG = 5

with open("data/flight_weighted_distances.csv", "r") as flight_data, open("data/flight_demand.csv") as flight_demand_data, open("data/flight_fuel_capacity.csv") as flight_fuel_data, open("data/aircraft.csv", "r") as aircraft_data:
    # 1. Import flight data
    reader = csv.reader(flight_data, delimiter=',')
    _ = next(reader)
    flights = [row for row in reader]
    
    # 2. Import flight demand data
    reader = csv.reader(flight_demand_data, delimiter=',')
    _ = next(reader)
    flight_demand = [row for row in reader]
    
    # 3. Import flight fuel data
    reader = csv.reader(flight_fuel_data, delimiter=',')
    _ = next(reader)
    flight_fuel = [row for row in reader]
    
    # 4. Import aircraft data
    reader = csv.reader(aircraft_data, delimiter=',')
    _ = next(reader)
    aircrafts = [row for row in reader]
    
    with open("data/flights.csv", "w") as outfile:
        outfile.write("source airport,destination airport,aircraft type,distance (weighted in km),number of passengers for 2% market share (flight demand), fuel (gallons)\n")
        
        for row_flight, row_flight_demand, row_flight_fuel in zip(flights, flight_demand, flight_fuel):
            assert row_flight[SOURCE_AIRPORT] == row_flight_demand[SOURCE_AIRPORT]
            assert row_flight[DESTINATION_AIRPORT] == row_flight_demand[DESTINATION_AIRPORT]
            assert row_flight[DESTINATION_AIRPORT] == row_flight_fuel[DESTINATION_AIRPORT]
            
            CURRENT_AIRCRAFT_INDEX = 2     # current index of aircraft type. Starts at 2, goes up to the total number of aircraft types.
            for aircraft in aircrafts:
                outfile.write(f"{row_flight[SOURCE_AIRPORT]},{row_flight_demand[DESTINATION_AIRPORT]},{aircraft[AIRCRAFT]},{row_flight[DISTANCE_KM]},{row_flight_demand[NUM_PASSENGERS]},{row_flight_fuel[CURRENT_AIRCRAFT_INDEX]}\n")
                CURRENT_AIRCRAFT_INDEX += 1
            
            