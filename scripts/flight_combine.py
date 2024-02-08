# Team: Foobar
# Authors: Anthony Cox
# Date: 1/31/2024
# Script: flight_demand.py
# Depends on: "data/airports.csv", "flight_distance.csv"
# Input: 
#   Lists of the source and destination airports and the distancce between them and the flight demand for them
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

with open("data/flight_weighted_distances.csv", "r") as flight_data, open("data/flight_demand.csv") as flight_demand_data:
    # 1. Import flight data
    reader = csv.reader(flight_data, delimiter=',')
    _ = next(reader)
    flights = [row for row in reader]
    
    # 2. Import flight demand data
    reader = csv.reader(flight_demand_data, delimiter=',')
    _ = next(reader)
    flight_demand = [row for row in reader]
    
    with open("data/flights.csv", "w") as outfile:
        outfile.write("source airport,destination airport,distance (weighted in km),number of passengers for 2% market share (flight demand)\n")
        
        for row_flight, row_flight_demand in zip(flights, flight_demand):
            assert row_flight[SOURCE_AIRPORT] == row_flight_demand[SOURCE_AIRPORT]
            assert row_flight[DESTINATION_AIRPORT] == row_flight_demand[DESTINATION_AIRPORT]
            
            outfile.write(f"{row_flight[SOURCE_AIRPORT]},{row_flight_demand[DESTINATION_AIRPORT]},{row_flight[DISTANCE_KM]},{row_flight_demand[NUM_PASSENGERS]}\n")
        