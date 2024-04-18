# Team: Foobar
# Authors: Anthony Cox
# Date: 1/31/2024
# Script: flight_distance.py
# Depends on: "data/airports.csv"
# Input: 
#   A list of the airport names and their geocoordinates (latitude and longitude)
# Output: 
#   A filtered list of each pair of airports and the distance (in km) between them.
#   The list is filtered to exclude flights closer than the minimum allowed distance.


import csv
from haversine import haversine, Unit

RANK = 0
NAME = 1
IATA = 2
CITY = 3
STATE = 4
METRO_AREA = 5
METRO_POPULATION = 6
LATITUDE = 7
LONGITUDE = 8

MINIMUM_ALLOWED_FLIGHT_DISTANCE = 240 # KM

with open('data/airports.csv', 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    _ = next(reader)
    airports = [airport for airport in reader]

    with open('data/flight_distance.csv', 'w') as outfile:
        outfile.write("source airport,destination airport,distance (km)\n")
        
        for source_airport in airports:
            for destination_airport in airports:
                distance = haversine(                                                                \
                    (float(source_airport[LATITUDE]),float(source_airport[LONGITUDE])),              \
                    (float(destination_airport[LATITUDE]),float(destination_airport[LONGITUDE])),    \
                    unit=Unit.KILOMETERS                                                             \
                )
                
                if distance >= MINIMUM_ALLOWED_FLIGHT_DISTANCE:
                    outfile.write(f'{source_airport[NAME]},{destination_airport[NAME]},{distance}\n')