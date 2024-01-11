import csv

RANK = 0
NAME = 1
IATA = 2
CITY = 3
STATE = 4
METRO_POPULATION = 5
LATITUDE = 6
LONGITUDE = 7

with open('data/airports.csv') as file:
    reader = csv.reader(file, delimiter=',',)
    next(reader)
    
    airports = []
    
    for row in reader:
        airports.append(row)
    
    for airport in airports:
        print(airport[NAME])
    