import csv
from pprint import pprint

# Indices of values in airports.csv
RANK = 0
NAME = 1
IATA = 2
CITY = 3
STATE = 4
METRO_AREA = 5
METRO_POPULATION = 6
LATITUDE = 7
LONGITUDE = 8

# Indices of values in flights.csv
SOURCE_AIRPORT = 0
DESTINATION_AIRPORT = 1
DISTANCE_KM = 2
DEMAND = 3

# aircraft_specs.csv
# aircraft,passenger_capacity,cruise_speed (km/h),max_fuel_capacity (gallons),max_range (km),mpg (mpg)
AIRCRAFT = 0
CAPACITY = 1
SPEED = 2
MAX_FUEL = 3
MAX_RANGE = 4
MPG = 5

# Formula constants
DAILY_DEMAND = 0.005
MARKET_SHARE = 0.02
KNOTS_TO_KPH = 1.852
MILES_TO_KM = 1.60934


# File-reading constants
FILE_START = 0

with open ("data/airports.csv", "r") as airport_data,open ("data/aircraft_specs.csv", "r") as aircraft_spec_data, open("data/flights.csv", "r") as flight_data, open("data/flight_time.csv", "w") as outfile:
    #make readers for files
    airport_reader = csv.reader(airport_data, delimiter=',')
    _ = next(airport_reader)
    flight_reader = csv.reader(flight_data, delimiter=',')
    _ = next(flight_reader)
    aircraft_reader = csv.reader(aircraft_spec_data, delimiter=',')
    _ = next(aircraft_reader)
    # write header of csv
    outfile.write("source airport, destination airport,airplane type, taxi time, total time")

    #
    metro_population = dict((airport[NAME],int(airport[METRO_POPULATION])) for airport in airport_reader)


    for row_flight in flight_reader:  # Iterate over the reader object, not the file object
        source_airport = row_flight[SOURCE_AIRPORT]
        destination_airport = row_flight[DESTINATION_AIRPORT]
        demand = float(row_flight[DEMAND])
        distance_km = float(row_flight[DISTANCE_KM])
        metro_population[row_flight[SOURCE_AIRPORT]]

        for row_aircraft_spec in aircraft_reader: 
            aircraft_name = row_aircraft_spec[AIRCRAFT]
            capacity = int(row_aircraft_spec[CAPACITY])
            cruise_speed = int(row_aircraft_spec[SPEED])
            mpg = float(row_aircraft_spec[MPG])

            total_time = 0
            speed = 0

            #calc cruising altitude
            cruising_altitude = 0
            #international
            if(source_airport == "Paris Charles de Gaulle Airport" or destination_airport == "Paris Charles de Gaulle Airport"):
                cruising_altitude = 38,000
            elif(distance_km >= 1500*MILES_TO_KM):
                cruising_altitude = 35,000
            elif(distance_km < 1500*MILES_TO_KM):
                cruising_altitude = 30,000

            #calc taxi time
            #if(airport == hub):
            #    taxi_time = 15
            #   if(metro_population <= 9,000,000):
            #  
            #   else:
            #       metro_pop_extra = (metro_population-9,000,000)
            #       while metro_pop_extra >0:
            #            taxi_time+=1
            #            metro_pop_extra -=2,000,000
            #
            taxi_time = min(13, metro_population*0.0000075)

            total_time += taxi_time
            #2. calc runway time
            #leaving
            #
            total_time+=1
            #landing
            total_time+=2
            







    
    
    