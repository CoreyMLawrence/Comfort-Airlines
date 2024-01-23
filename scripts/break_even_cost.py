import csv

# Indices of values in flight_demand.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DISTANCE_KM = 2
DEMAND = 3

#aircraftSpecs.csv, fucked for time: mpg, seats
Boeing_737_600 = .55, 119
Boeing_767_800  = .44, 189
Airbus_A200_100 = .57, 135
Airbus_A200_300 = .66, 160


# Formula constants
takeoff_fee = 2000
landing_fee = 2000
gas = 6.19#gallon
KMtoM = 0.621371#converst to miles
percent_full = .333

# File-reading constants
FILE_START = 0


with open ("data/flights.csv", "r") as flights: # open ("data/aircraftSpecs.csv", "r") as aircraft:
    #Generate break even costs
    reader = csv.reader(flights, delimiter=',')
    #skip header row
    header = next(reader)
    
    for row in reader:  # Iterate over the reader object, not the file object
        source_airport = row[SOURCE_AIRPORT]
        destination_airport = row[DESTINATION_AIRPORT]
        demand = float(row[DEMAND])
        distance_km = float(row[DISTANCE_KM])

        # Calculate total cost
        total_cost = (distance_km * KMtoM / Boeing_737_600[0]) * gas+takeoff_fee+landing_fee
        
        #calculate break even at 30% capacity
        break_even_cost_per_ticket = total_cost/(Boeing_737_600[1]*percent_full)

        # Print information
        print(f"Source: {source_airport}, Destination: {destination_airport}")
        print(f"Demand: {demand}, Distance: {distance_km} km")
        print(f"Total Cost: {total_cost}")
        print(f"Break Even Cost Per Ticket: {break_even_cost_per_ticket}")
        print()
