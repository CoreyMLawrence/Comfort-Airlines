import csv
from pprint import pprint

# Indices of values in flight_demand.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DEMAND = 2
DISTANCE_KM = 3

#aircraftSpecs.csv, fucked for time
Boeing_737_600 = .55 
Boeing_767_800  = .44
Airbus_A200_100 = .57
Airbus_A200_300 = .66


# Formula constants
takeoff_fee = 2000
landing_fee = 2000
gas = 6.19#gallon
KMtoM = 0.621371#converst to miles

# File-reading constants
FILE_START = 0


with open ("data/flights.csv", "r") as flights:
    #Generate break even costs
    reader = csv.reader(flights, delimiter=',')
    header = next(reader)
    for row in flights:
        print(row[SOURCE_AIRPORT], row[DESTINATION_AIRPORT])
        print(row[DEMAND], row[DISTANCE_KM])
        print(row[DISTANCE_KM]*KMtoM/Boeing_737_600*gas)


