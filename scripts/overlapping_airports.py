# Team: Foobar
# Authors: Anthony Cox
# Date: 1/31/2024
# Script: overlapping_airports.py
# Depends on: "data/airports.csv"
# Input: 
#   A list of the airport names and their metro areas
# Output: 
#   A filtered mapping of metro areas to airports where the airports 
#   share the same metro area
#
# Note: one-time script. do not run again.

import csv
from pprint import pprint

# CSV data indices
RANK = 0
NAME = 1
IATA = 2
CITY = 3
STATE = 4
METRO_AREA = 5
METRO_POPULATION = 6
LATITUDE = 7
LONGITUDE = 8

# Dictionary constants
KEY = 0
VALUE = 1

with open("data/airports.csv", "r") as infile:
    reader = csv.reader(infile, delimiter=',')
    _ = next(reader)
    airports = [row for row in reader]
    metro_areas = {}

    for airport in airports:
        if airport[METRO_AREA] in metro_areas:
            metro_areas[airport[METRO_AREA]].append(airport[NAME])
        else:
            metro_areas[airport[METRO_AREA]] = [airport[NAME]]

    pprint(dict(filter(lambda entry: len(entry[VALUE]) > 1, metro_areas.items())))