#Parker Blue
#script that runs all possibe flight combinations  (4 plane types, 800+routes)
# and creates csvs of profitable and loss flights separately
# NOTE: does not account for (max) fuel capacity, refuel, etc, purely monetary calc
#only accounts for generic takeoff/landing fee (4k total) and gas @ 6.19 a gallon

import csv


# Indices of values in flights.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DISTANCE_KM = 2
DEMAND = 3

# aircraft.csv
# aircraft,passenger_capacity,cruise_speed (km/h),max_fuel_capacity (gallons),max_range (km),mpg (mpg)
AIRCRAFT = 0
CAPACITY = 1
SPEED = 2
MAX_FUEL = 3
MAX_RANGE = 4
MPG = 5

# fuel_capacity.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
FUEL_737_600 = 2
FUEL_737_800 = 3
FUEL_A200 = 4
FUEL_A220 = 5


# Formula constants
takeoff_fee = 2000
landing_fee = 2000
gas = 6.19              # gallons
KMtoM = 0.621371        # converts to miles
break_even_percentage = 0.3
#cruise_speed_factor = .9

# File-reading constants
FILE_START = 0


with open ("data/flights.csv", "r") as flight_data, open ("data/aircraft.csv", "r") as aircraft_spec_data,open ("data/flight_fuel_capacity.csv") as fuel_data, open("data/flight_profit_per_hour.csv", "w") as outfile:
    #Generate break even costs
    flight_reader = csv.reader(flight_data, delimiter=',')
    aircraft_spec_reader = csv.reader(aircraft_spec_data, delimiter=',')
    fuel_reader = csv.reader(fuel_data, delimiter=',')
    
    #write header of outfile outside loop
    outfile.write("source airport,destination airport,airplane type,flight_hours,total Cost,break even cost per ticket, profit/loss per flight,profit/loss per hour, percent full\n")
    #skip header row
    _ = next(flight_reader)
    _ = next(aircraft_spec_reader)
    
    #uncomment all of the lines with running_total to get a total profit/loss for all possible flights
    #running_total = 0
    
    for row_flight in flight_reader:  # Iterate over the reader object, not the file object
        source_airport = row_flight[SOURCE_AIRPORT]
        destination_airport = row_flight[DESTINATION_AIRPORT]
        demand = float(row_flight[DEMAND])
        distance_km = float(row_flight[DISTANCE_KM])

        for row_aircraft_spec in aircraft_spec_reader: 
            aircraft_name = row_aircraft_spec[AIRCRAFT]
            capacity = int(row_aircraft_spec[CAPACITY])
            cruise_speed = int(row_aircraft_spec[SPEED])
            mpg = float(row_aircraft_spec[MPG])

            # Calculate total cost
            total_cost = (distance_km * KMtoM / mpg ) * gas + takeoff_fee + landing_fee
            
            #calculate break even at 30% capacity
            break_even_cost_per_ticket = total_cost / (capacity * break_even_percentage)
            
            #calculate profit/loss per flight
            profit_loss = break_even_cost_per_ticket * demand - total_cost
            #running_total +=profit_loss

            #calc percent full
            percent_full = demand/capacity
            
            #calc flight hours
            flight_hours = distance_km/cruise_speed
            
            #calc profit/hour
            profit_per_hour = profit_loss/flight_hours

            #4. Write body
            if profit_loss>0:
                outfile.write(f"{source_airport},{destination_airport},{aircraft_name},{flight_hours},{total_cost},{break_even_cost_per_ticket},{profit_loss},{profit_per_hour},{percent_full}\n")
            
            # Print information
            #print(f"Source: {source_airport}, Destination: {destination_airport}")
            #print(f"Demand: {demand}, Distance: {distance_km} km")
            #print(f"Total Cost: {total_cost}")
            #print(f"Break Even Cost Per Ticket: {break_even_cost_per_ticket}")
            #print(f"Using the model: {aircraft_name} aircraft")
            #print()
        
        aircraft_spec_data.seek(FILE_START)
        _ = next(aircraft_spec_reader)
        
#print(running_total)
