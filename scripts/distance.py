import csv
from scripts.haversine import haversine, Unit

RANK = 0
NAME = 1
IATA = 2
CITY = 3
STATE = 4
METRO_AREA = 5
METRO_POPULATION = 6
LATITUDE = 7
LONGITUDE = 8

with open('data/airports.csv') as infile:
    reader = csv.reader(infile, delimiter=',',)
    _ = next(reader)
    airports = [row for row in reader]

    with open('data/distance.csv', 'w') as outfile:
        for source_airport in airports:
            for destination_airport in airports:
                distance = haversine(                                                                \
                    (float(source_airport[LATITUDE]),float(source_airport[LONGITUDE])),              \
                    (float(destination_airport[LATITUDE]),float(destination_airport[LONGITUDE])),    \
                    unit=Unit.KILOMETERS                                                             \
                )

                outfile.write(f'{source_airport[NAME]},{destination_airport[NAME]},{distance}\n')