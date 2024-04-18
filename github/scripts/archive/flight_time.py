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

# aircraft.csv
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
ASCENT_ANGLE = 6


# File-reading constants
FILE_START = 0

with open ("data/airports.csv", "r") as airport_data,open ("data/aircraft.csv", "r") as aircraft_spec_data, open("data/flights.csv", "r") as flight_data, open("data/flight_time.csv", "w") as outfile:
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
            cruise_speed = int(row_aircraft_spec[SPEED])*(.8/.9) #for converting to 80% of max speed from 90
            mpg = float(row_aircraft_spec[MPG])

            #variables
            total_time = 0 #minutes
            speed = 0#converted to kph
            cruising_altitude = 0#feet
            current_altitude = 0#feet
            
            
            #calc cruising altitude
            #international
            if(source_airport == "Paris Charles de Gaulle Airport" or destination_airport == "Paris Charles de Gaulle Airport"):
                cruising_altitude = 38,000
            elif(distance_km >= 1500*MILES_TO_KM):
                cruising_altitude = 35,000
            elif(distance_km >=350*MILES_TO_KM):
                cruising_altitude = 30,000
            elif(distance_km >=200*MILES_TO_KM):
                cruising_altitude = 25,000
            else:
                cruising_altitude = 20,000

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
            #else:
            taxi_time = min(13, metro_population*0.0000075)

            total_time += taxi_time
            #calc runway time
            #leaving
            total_time+=1
            speed = 150*KNOTS_TO_KPH
            
            #calc cruise time
            ascend_speed = 250
            acceleration_speed = 280
            acceleration_rate = 25
            descent_rate = 1000 / (3 * KNOTS_TO_KPH)  # Descent rate in feet per kilometer
            descent_speed = 250
            landing_speed = 200
            deceleration_rate = 35
            
            while current_altitude< cruising_altitude:
                # Ascend at 6 degrees
                current_altitude += ascend_speed * (1 / 60)  # Assuming 1 minute intervals
                total_time += 1 / 60  # Incrementing time
                
                # Check if altitude is below 10,000 feet for acceleration
                if current_altitude <= 10000:
                    current_speed = ascend_speed
                else:
                    # Accelerate until cruising altitude is reached
                    if current_speed < acceleration_speed:
                        current_speed += acceleration_rate * (1 / 60)
                    elif current_speed > acceleration_speed:
                        current_speed = acceleration_speed
                    
                    # Ensure speed does not exceed 80% of the maximum speed
                    if current_speed >cruise_speed:
                        current_speed =cruise_speed
                
                #check if descent should start
                if current_altitude >= cruising_altitude:
                    # Calculate distance traveled during descent
                    descent_distance = (current_altitude - cruising_altitude) / descent_rate
                    
                    # Update altitude and speed during descent
                    while descent_distance > 0:
                        if current_altitude > 10000:
                            current_speed = descent_speed
                        else:
                            current_speed = landing_speed if current_speed > landing_speed else current_speed
                            
                        descent_distance -= current_speed / 60  # Assuming 1 minute intervals
                        current_altitude -= descent_rate / 60  # Assuming 1 minute intervals
                        total_time += 1 / 60  # Incrementing time
                        
                        # Decelerate at a constant rate
                        current_speed -= deceleration_rate * (1 / 60)
                        current_speed = max(current_speed, 0) 
                                    
                    
            
            
            
            
            
            
            
            #calc runway time
            #landing
            total_time+=2

            







    
    
    