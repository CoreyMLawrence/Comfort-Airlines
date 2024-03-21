# Team: Foobar
# Authors: Parker Blue, Zach 
# Date: 1/31/2024
# Script: flight_master_record.py
# Depends on: "flight_times.csv", "flights.csv", "flight_profit_or_loss.csv"
# Input: 
#   Lists of the source and destination airports and the distance between them, the flight demand for them, profit for them
# Output: 
#   An aggregated list of the lists

"""
    This is the master record generator that is fed into the simulation, 
    it uses the output of flight_times.py, and flight_profit_or_loss.py, and the previous combination script of flight_combine.py
    flight_combine combines "airports.csv", "flight_distance.csv", "flight_fuel_capacity.csv". 
    there is a master runner script "pipeline.ps1" that recalculates everything from the start, reference that for execution order.
    This outputs an aggregate of all data needed to start/run the simulation
    
"""


import csv



# Indices of values in flights.csv
# source airport,destination airport,distance (weighted in km),number of passengers for 2% market share (flight demand),name,fuel
FLIGHTS_SOURCE_AIRPORT = 0
FLIGHTS_DESTINATION_AIRPORT = 1
FLIGHTS_DISTANCE_KM = 2
FLIGHTS_NUM_PASSENGERS = 3
FLIGHTS_AIRCRAFT_TYPE = 4
FLIGHTS_FUEL = 5

# Indices of values in flight_profit_or_loss.csv
# source airport,destination airport,airplane type,total Cost,break even cost per ticket, profit/loss per flight, percent full
PROFITS_SOURCE_AIRPORT = 0
PROFITS_DESTINATION_AIRPORT = 1
PROFITS_AIRCRAFT_TYPE = 2
PROFITS_TOTAL_COST = 3
PROFITS_COST_PER_TICKET = 4
PROFITS_PROFIT_PER_FLIGHT = 5
PROFITS_PERCENT_FULL = 6

# Indices of values in flight times docs
# source,destination,airplane type,time
TIMES_SOURCE_AIRPORT = 0
TIMES_DESTINATION_AIRPORT = 1
TIMES_AIRCRAFT_TYPE = 2
TIMES_FLIGHT_TIME = 3

#all of this should be fine, just rips all relevant data from each file and makes a dict of each of them
with open("data/flights.csv", "r") as flight_data, open("data/flight_profit_or_loss.csv") as flight_profit_data, open("data/flight_times.csv") as flight_time_data:
    reader = csv.reader(flight_data, delimiter=',')
    _ = next(reader)
    flights = [row for row in reader]

    reader = csv.reader(flight_profit_data, delimiter=',')
    _ = next(reader)
    profits = [row for row in reader] 

    reader = csv.reader(flight_time_data, delimiter=',')
    _ = next(reader)
    times = [row for row in reader] 
    #start editing here i think unless i fucked something, format/edit as necessary
    with open("data/flight_master_record.csv", "w") as outfile:
        outfile.write("source airport, destination airport, distance (weighted km), fuel, number of passengers, aircraft type, expected time, ticket cost, net profit\n")
        for row_flights, row_profits, row_times in zip(flights, profits, times):
            #may need more asserts to match each entry
            assert row_flights[FLIGHTS_SOURCE_AIRPORT] == row_profits[PROFITS_SOURCE_AIRPORT]
            assert row_flights[FLIGHTS_DESTINATION_AIRPORT] == row_profits[PROFITS_DESTINATION_AIRPORT]
            
            assert row_flights[FLIGHTS_SOURCE_AIRPORT] == row_times[TIMES_SOURCE_AIRPORT]
            assert row_flights[FLIGHTS_DESTINATION_AIRPORT] == row_times[TIMES_DESTINATION_AIRPORT]
            
            assert row_flights[FLIGHTS_AIRCRAFT_TYPE] == row_profits[PROFITS_AIRCRAFT_TYPE]
            assert row_flights[FLIGHTS_AIRCRAFT_TYPE] == row_times[TIMES_AIRCRAFT_TYPE]
        
            
            #print(f"{row_flights[FLIGHTS_SOURCE_AIRPORT]},{row_flights[FLIGHTS_DESTINATION_AIRPORT]},{row_flights[FLIGHTS_DISTANCE_KM]},{row_flights[FLIGHTS_NUM_PASSENGERS]},{row_times[TIMES_AIRCRAFT_TYPE]},{row_times[TIMES_FLIGHT_TIME]},{row_profits[PROFITS_COST_PER_TICKET]},{row_profits[PROFITS_PROFIT_PER_FLIGHT]}")
            
            outfile.write(f"{row_flights[FLIGHTS_SOURCE_AIRPORT]},{row_flights[FLIGHTS_DESTINATION_AIRPORT]},{row_flights[FLIGHTS_DISTANCE_KM]},{row_flights[FLIGHTS_FUEL]},{row_flights[FLIGHTS_NUM_PASSENGERS]},{row_times[TIMES_AIRCRAFT_TYPE]},{row_times[TIMES_FLIGHT_TIME]},{row_profits[PROFITS_COST_PER_TICKET]},{row_profits[PROFITS_PROFIT_PER_FLIGHT]}\n")