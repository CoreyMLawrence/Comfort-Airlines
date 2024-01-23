import csv
from pprint import pprint

# Indices of values in flight_demand.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DEMAND = 2
DISTANCE_KM = 3


# Formula constants
takeoff_fee = 2000
landing_fee = 2000
gas = 6.19#gallon

# File-reading constants
FILE_START = 0


with open ("data/flight_demand.csv", "r") as flight_demand, open("data/flights.csv", "r") as flight_data:
    # 1. Generete a mapping of airports to their metro populations
    reader = csv.reader(flight_demand, delimiter=',')
    header = next(reader)
    metro_population = dict(
        (airport[NAME],int(airport[METRO_POPULATION])) for airport in reader
    )



#extracting distances from distance matrix.csv
for i in range(31):
    for j in range(i+1, 31):
        #grab distance from csv