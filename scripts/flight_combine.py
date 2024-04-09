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
FUEL_BOEING_737_600 = 2
FUEL_BOEING_767_800 = 3
FUEL_AIRBUS_A200_100 = 4
FUEL_AIRBUS_A220_300 = 5
FUEL_BOEING_747_400 = 6

with open("data/flight_weighted_distances.csv", "r") as flight_data, open("data/flight_demand.csv") as flight_demand_data, open("data/flight_fuel_capacity.csv") as flight_fuel_data:
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
    
    with open("data/flights.csv", "w") as outfile:
        outfile.write("source airport,destination airport,aircraft type,distance (weighted in km),number of passengers for 2% market share (flight demand), fuel (gallons)\n")
        
        for row_flight, row_flight_demand, row_flight_fuel in zip(flights, flight_demand, flight_fuel):
            assert row_flight[SOURCE_AIRPORT] == row_flight_demand[SOURCE_AIRPORT]
            assert row_flight[DESTINATION_AIRPORT] == row_flight_demand[DESTINATION_AIRPORT]
            assert row_flight[DESTINATION_AIRPORT] == row_flight_fuel[DESTINATION_AIRPORT]
            

            outfile.write(f"{row_flight[SOURCE_AIRPORT]},{row_flight_demand[DESTINATION_AIRPORT]},Boeing 737-600,{row_flight[DISTANCE_KM]},{row_flight_demand[NUM_PASSENGERS]},{row_flight_fuel[FUEL_BOEING_737_600]}\n")
            outfile.write(f"{row_flight[SOURCE_AIRPORT]},{row_flight_demand[DESTINATION_AIRPORT]},Boeing 767-800,{row_flight[DISTANCE_KM]},{row_flight_demand[NUM_PASSENGERS]},{row_flight_fuel[FUEL_BOEING_767_800]}\n")
            outfile.write(f"{row_flight[SOURCE_AIRPORT]},{row_flight_demand[DESTINATION_AIRPORT]},Airbus A200-100,{row_flight[DISTANCE_KM]},{row_flight_demand[NUM_PASSENGERS]},{row_flight_fuel[FUEL_AIRBUS_A200_100]}\n")
            outfile.write(f"{row_flight[SOURCE_AIRPORT]},{row_flight_demand[DESTINATION_AIRPORT]},Airbus A220-300,{row_flight[DISTANCE_KM]},{row_flight_demand[NUM_PASSENGERS]},{row_flight_fuel[FUEL_AIRBUS_A220_300]}\n")
            outfile.write(f"{row_flight[SOURCE_AIRPORT]},{row_flight_demand[DESTINATION_AIRPORT]},Boeing 747-400,{row_flight[DISTANCE_KM]},{row_flight_demand[NUM_PASSENGERS]},{row_flight_fuel[FUEL_BOEING_747_400]}\n")
            
            