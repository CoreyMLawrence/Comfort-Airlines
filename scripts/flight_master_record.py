# Team: Foobar
# Authors: Parker Blue, Zach 
# Date: 1/31/2024
# Script: flight_master_record.py
# Depends on: "flight_times_(Airbus_A200-100/300, Boeing_737-600/800)".csv, "flights.csv", "flight_profit_or_loss.csv"
# Input: 
#   Lists of the source and destination airports and the distance between them, the flight demand for them, profit for them,
# Output: 
#   An aggregated list of the lists

import csv

"""
    FOR ZACH:
    Corey will be making an all-in-one flight_times.csv in the format shown below, all you should have to do is:
    
    (correctly) zip the files together into one coherent csv and output the proper stuff. 
    My first approach was to elif the 4 kinds of planes and "manually" zip them togther, you can continue that way or find another,
    my checks are commented out for ease
    The outfile requirements (what each of the columns are) are all correct, feel free to double check.
    the output (the .write in the loop) will also need edited, should only be 1-2 fields (there is an arrow to it below),
    related to the type/time (i did most of them right)
    
    this whole thing will then be used as the basis for the flights class, 
    but that will be trivial if all the needed info is in this things csv output file.
    
    basically just making one csv with all the class needs in one place
    
    
    
 """




# Indices of values in flights.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DISTANCE_KM = 2
NUM_PASSENGERS = 3
FUEL_B600 = 4
FUEL_B800 = 5
FUEL_A100 = 6
FUEL_A300 = 7

# Indices of values in flight_profit_or_loss.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
TYPE = 2
TOTAL_COST = 3
COST_PER_TICKET = 4
PROFIT_PER_FLIGHT = 5
PERCENT_FULL = 6

# Indices of values in flight times docs
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
TYPE = 2
TIME = 3

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
        outfile.write("source airport, destination airport, distance (weighted km), number of passengers, expected time(737-600), expected time(767-800), expected time(A200-100),expected time(A220-300), Cost Per Ticket, Profit/Loss\n")
        for row_flights, row_profits, row_times in zip(flights, profits, times):
            #may need more asserts to match each entry
            assert row_flights[SOURCE_AIRPORT] == row_profits[SOURCE_AIRPORT]
            assert row_flights[DESTINATION_AIRPORT] == row_profits[DESTINATION_AIRPORT]
            assert row_flights[DESTINATION_AIRPORT] == row_times[DESTINATION_AIRPORT]
            
            
            #if row_times[TYPE] == row_profit[TYPE] == Airbus A220-100:
            #elif row_times[TYPE] == row_profit[TYPE] == Airbus A220-300:
            #elif row_times[TYPE] == row_profit[TYPE] == Boeing 737-600:
            #elif row_times[TYPE] == row_profit[TYPE] == Boeing 737-800:
            
            outfile.write(f"{row_flights[SOURCE_AIRPORT]},{row_flights[DESTINATION_AIRPORT]},\
                          {row_flights[DISTANCE_KM]},{row_flights[NUM_PASSENGERS]},\
                          {row_times[TYPE]}, {row_times [TIME]},\
                          {row_profits[COST_PER_TICKET]},{row_profits[PROFIT_PER_FLIGHT]}\n")