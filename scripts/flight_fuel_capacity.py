import csv
from pprint import pprint

# Indices of values in linear_aircraft_specs.csv
AIRCRAFT = 0
PASSENGER_CAPACITY = 1
CRUISE_SPEED = 2
MAX_FUEL_CAPACITY = 3
MAX_RANGE = 4
MPG = 5

# Indices of values in flight_distance.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DISTANCE = 2

# Formula constants
MPG_2_KPG = 1.609   # (MPG*1.609 = KPG)
DESIRED_FUEL_MULTIPLIER = 1.3    # Amount of fuel we want for flights (130% of fuel required to complete a flight).

# File-reading constants
FILE_START = 0

with open ("data/aircraft_specs.csv", "r") as aircraft_data, open("data/flight_distance.csv", "r") as flight_data:
    # 1. Import aircraft data
    reader = csv.reader(aircraft_data, delimiter=',')
    _ = next(reader)
    aircrafts = [row for row in reader]
    
    # 2. Import flight data
    reader = csv.reader(flight_data, delimiter=',')
    _ = next(reader)
    flights = [row for row in reader]
    
    # 4. Calculate the KPG and output the amount of fuel needed for the next flight in gallons (The amount of fuel is 130% of the fuel needed to make the trip).
    with open("data/flight_fuel_capacity.csv", "w") as outfile:
        # 4A. Write Headers (prints out each airplane's name)
        header_output = ""
        for aircraft in aircrafts:
            header_output += (",Fuel for " + aircraft[AIRCRAFT] + " (Gallons)")
        outfile.write("source airport,destination airport" + header_output + "\n")
        
        # 4B. Calculate KPG and write body
        for flight in flights:
            flight_distance = float(flight[DISTANCE])
            kpg_output = ""
            for aircraft in aircrafts:
                flight_kpg = (float(aircraft[MPG]) * MPG_2_KPG)
                flight_fuel = (flight_distance / flight_kpg) * DESIRED_FUEL_MULTIPLIER
                kpg_output += ("," + str(flight_fuel))
            
            outfile.write(flight[SOURCE_AIRPORT] + "," + flight[DESTINATION_AIRPORT] + kpg_output + "\n")