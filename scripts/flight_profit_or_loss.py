#Parker Blue
#script that runs all possibe flight combinations  (4 plane types, 800+routes)
# and creates csvs of profitable and loss flights separately
# NOTE: does not account for (max) fuel capacity, refuel, etc, purely monetary calc
#only accounts for generic takeoff/landing fee (4k total) and gas @ 6.19 a gallon

import csv


# Indices of values in flights.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
AIRCRAFT_TYPE = 2
DISTANCE_KM = 3
DEMAND = 4
FUEL_REQUIRED = 5

MPG = {
    "Boeing 737-600" : 0.55,
    "Boeing 767-800" : 0.44,
    "Airbus A200-100" : 0.57,
    "Airbus A220-300" : 0.66,
    "Boeing 747-400" : 0.22
}

CAPACITY = {
    "Boeing 737-600" : 119,
    "Boeing 767-800" : 189,
    "Airbus A200-100" : 135,
    "Airbus A220-300" : 160,
    "Boeing 747-400" : 416
}

# Formula constants
takeoff_fee = 2000
landing_fee = 2000
gas = 6.19              # gallons
KMtoM = 0.621371        # converts to miles
break_even_percentage = 0.3

# File-reading constants
FILE_START = 0


with open ("data/flights.csv", "r") as flight_data, open("data/flight_profit_or_loss.csv", "w") as outfile1:# open("data/flight_profit_or_loss_loss.csv", "w") as outfile2:
    #Generate break even costs
    flight_reader = csv.reader(flight_data, delimiter=',')
    
    #write header of outfile outside loop
    outfile1.write("source airport,destination airport,airplane type,total Cost,break even cost per ticket, profit/loss per flight, percent full\n")
    #outfile2.write("source airport,destination airport,airplane type,total Cost,break even cost per ticket, loss per flight, percent full\n")
    #skip header row
    _ = next(flight_reader)
    
    #uncomment all of the lines with running_total to get a total profit/loss for all possible flights
    #running_total = 0
    
    for row_flight in flight_reader:  # Iterate over the reader object, not the file object
        source_airport = row_flight[SOURCE_AIRPORT]
        destination_airport = row_flight[DESTINATION_AIRPORT]
        demand = float(row_flight[DEMAND])
        distance_km = float(row_flight[DISTANCE_KM])
        aircraft_name = row_flight[AIRCRAFT_TYPE]
        capacity = int(CAPACITY[row_flight[AIRCRAFT_TYPE]])
        mpg = float(MPG[row_flight[AIRCRAFT_TYPE]])


        #clac
        # Calculate total cost
        total_cost = (distance_km * KMtoM / mpg ) * gas + takeoff_fee + landing_fee
        
        #calculate break even at 30% capacity
        break_even_cost_per_ticket = total_cost / (capacity * break_even_percentage)
        
        #calculate profit/loss per flight
        profit_loss = break_even_cost_per_ticket * demand - total_cost
        #running_total +=profit_loss

        percent_full = demand/capacity

        #4. Write body
        #if profit_loss > 0:
        outfile1.write(f"{source_airport},{destination_airport},{aircraft_name},{total_cost},{break_even_cost_per_ticket},{profit_loss},{percent_full}\n")
        # else:
            # outfile2.write(f"{source_airport},{destination_airport},{aircraft_name},{total_cost},{break_even_cost_per_ticket},{profit_loss},{percent_full}\n")
        
        # Print information
        #print(f"Source: {source_airport}, Destination: {destination_airport}")
        #print(f"Demand: {demand}, Distance: {distance_km} km")
        #print(f"Total Cost: {total_cost}")
        #print(f"Break Even Cost Per Ticket: {break_even_cost_per_ticket}")
        #print(f"Using the model: {aircraft_name} aircraft")
        #print()
        
#print(running_total)
