import csv
#NOTE: does not account for (max) fuel capacity, purely monetary calc

# Indices of values in flight_demand.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DISTANCE_KM = 2
DEMAND = 3

#linear_aircraft_specs.csv
#aircraft,passenger_capacity,cruise_speed (km/h),max_fuel_capacity (gallons),max_range (km),mpg (mpg)
AIRCRAFT = 0
CAPACITY = 1
SPEED = 2
MAX_FUEL = 3
MAX_RANGE = 4
MPG = 5


# Formula constants
takeoff_fee = 2000
landing_fee = 2000
gas = 6.19#gallon
KMtoM = 0.621371#converts to miles
percent_full = .333

# File-reading constants
FILE_START = 0


with open ("data/flights.csv", "r") as flights, open ("data/linear_aircraft_specs.csv", "r") as aircraft, open("data/cost_per_flight.csv", "w") as outfile:
    #Generate break even costs
    reader1 = csv.reader(flights, delimiter=',')
    reader2 = csv.reader(aircraft, delimiter=',')
    #write header of outfile outside loop
    outfile.write("source airport,destination airport,airplane type,total Cost,break even cost per ticket\n")

    #skip header row
    header1 = next(reader1)
    header2 = next(reader2)
    
    for row1 in reader1:  # Iterate over the reader object, not the file object
        source_airport = row1[SOURCE_AIRPORT]
        destination_airport = row1[DESTINATION_AIRPORT]
        demand = float(row1[DEMAND])
        distance_km = float(row1[DISTANCE_KM])


        for row2 in reader2: 
            aircraft_name = row2[AIRCRAFT]
            capacity = int(row2[CAPACITY])
            mpg = float(row2[MPG])




            # Calculate total cost
            total_cost = (distance_km * KMtoM / mpg ) * gas+takeoff_fee+landing_fee
            
            #calculate break even at 30% capacity
            break_even_cost_per_ticket = total_cost/( capacity * percent_full)


            #4. Write body
            outfile.write(f"{source_airport},{destination_airport},{aircraft_name},{total_cost},{break_even_cost_per_ticket}\n")
            # Print information
            #print(f"Source: {source_airport}, Destination: {destination_airport}")
            #print(f"Demand: {demand}, Distance: {distance_km} km")
            #print(f"Total Cost: {total_cost}")
            #print(f"Break Even Cost Per Ticket: {break_even_cost_per_ticket}")
            #print(f"Using the model: {aircraft_name} aircraft")
            #print()
        aircraft.seek(0)
        header2 = next(reader2)

#NOTE: does not account for (max) fuel capacity, purely monetary calc