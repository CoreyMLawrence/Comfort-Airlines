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