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

with open('data/airports.csv', 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    _ = next(reader)
    airports = [airport for airport in reader]

    with open('data/flight_distance.csv', 'w') as outfile:
        outfile.write("source airport, destination airport, distance (km)\n")
        
        for source_airport in airports:
            for destination_airport in airports:
                distance = haversine(                                                                \
                    (float(source_airport[LATITUDE]),float(source_airport[LONGITUDE])),              \
                    (float(destination_airport[LATITUDE]),float(destination_airport[LONGITUDE])),    \
                    unit=Unit.KILOMETERS                                                             \
                )
                
                if distance >= 240:
                    outfile.write(f'{source_airport[NAME]},{destination_airport[NAME]},{distance}\n')