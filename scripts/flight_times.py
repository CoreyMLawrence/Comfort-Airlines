"""
AUTHOR: Corey Lawrence

Script to calculate estimated flight times between pairs of airports, considering various factors such as taxi times,
ascent and descent times, ramp-up and ramp-down times, and cruising speeds.

This script reads airport data from a CSV file containing latitude and longitude information.
It then estimates the flight times between all pairs of airports, adjusting for the direction of travel.
The resulting estimated flight times are stored in a CSV file with columns for the origin airport,
destination airport, and the calculated flight time.

Functions:
    - taxi_time(population, airport): Calculates estimated taxi time based on airport population and hub status.
    - cruising_altitude(distance): Determines the cruising altitude based on the estimated trip distance.
    - ascent_time(trip_altitude): Calculates estimated ascent time and ground distance to reach cruising altitude.
    - ramp_up(CRUISE_SPEED, trip_altitude): Estimates ramp-up time and distance to reach cruise speed.
    - ramp_down(CRUISE_SPEED, trip_altitude): Estimates ramp-down time and distance to decelerate from cruise speed.
    - descent_time(trip_altitude): Calculates estimated descent time and ground distance from cruising altitude to landing.

Input:
    - 'airports.csv': CSV file containing airport data including latitude and longitude.
    - 'flight_weighted_distances.csv': CSV file containing estimated flight distances between pairs of airports.
Output:
    - 'flight_estimated_times.csv': CSV file containing the estimated flight times between pairs of airports.
"""

import math
import csv
import os

delete_itermediate_files = True

# Arrays to store aircraft names and cruise speeds
aircraft_names = []
cruise_speeds = []

aircraft_csv = '../data/aircraft.csv'

# Read aircraft data from the CSV file
with open(aircraft_csv, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        aircraft_name = row['aircraft']
        cruise_speed = float(row['max_speed (km/h)'])
        
        # Replace spaces with underscores in the file name
        output_file_name = f'flight_times_{aircraft_name.replace(" ", "_")}.csv'
        
        # Append aircraft name and cruise speed to arrays
        aircraft_names.append(output_file_name)
        cruise_speeds.append(cruise_speed)

        print("Aircraft Names List:", aircraft_names)


for i in range(len(aircraft_names)):
    CRUISE_SPEED = cruise_speeds[i] * .8
    output_csv_path = f"../data/{aircraft_names[i]}"

    # Function to calculate the taxi time for an airport
    def taxi_time(population, airport):
        """
        Calculates the taxi time for an airport based on its population and hub status.

        Args:
            population (float): Population of the airport's metropolitan area.
            airport (str): Name of the airport.

        Returns:
            float: Taxi time in minutes.
        """
        # List of major airport hubs
        hubs = ["Hartsfield-Jackson Atlanta International Airport",
            "Dallas/Fort Worth International Airport",
            "Denver International Airport",
            "O'Hare International Airport"]

        time = 0
        if airport not in hubs:
            time = population * 0.00075
            if time > 13:
                time = 13
        else:
            if population <= 9000000:
                time = 15
            else:
                time = 15 + ((population-9000000)/2000000)
                if time > 20:
                    time = 20
        return time

    # Function to determine cruising altitude based on trip distance
    def cruising_altitude(distance):
        """
        Determines the cruising altitude based on the trip distance.

        Args:
            distance (float): Distance of the trip.

        Returns:
            int: Cruising altitude in feet.
        """
        if distance >= 2414.016:
            return 35000
        elif distance >= 563.27:
            return 30000
        elif distance >= 321.869:
            return 25000
        else:
            return 20000

    # Function to calculate ascent time and ground distance
    def ascent_time(trip_altitude):
        print("\nInside ascent_time function:")
        print("trip_altitude:", trip_altitude)

        # Given data
        time_sum = 0
        ground_speed = 463  # kmph (250 knots)
        angle_of_ascent = math.radians(6)  # convert degrees to radians

        # Calculate vertical speed
        vertical_speed = ground_speed * math.sin(angle_of_ascent)

        # Altitude to ascend
        altitude_to_ascend = 10000  # feet

        # Calculate time to ascend to 10,000 feet
        time_to_10000_feet = altitude_to_ascend / vertical_speed / 60 # minutes
        ground_distance = ground_speed * time_to_10000_feet/60 #km
        time_sum += time_to_10000_feet
        trip_altitude -= 10000
        print("time_sum after first segment:", time_sum)
        print("trip_altitude after first segment:", trip_altitude)
        
        if (trip_altitude > 0):
            ground_speed = 518.56  # kmph (280 knots)

            # Calculate vertical speed
            vertical_speed = ground_speed * math.sin(angle_of_ascent)

            # Altitude to ascend
            altitude_to_ascend = trip_altitude  # feet

            # Calculate time to ascend to cruising altitude
            time_to_cruising_altitude = altitude_to_ascend / vertical_speed /60 # minutes
            ground_distance += ground_speed * time_to_cruising_altitude/60 #(km)
            time_sum += time_to_cruising_altitude
            print("time_sum after second segment:", time_sum)

        result = [time_sum, ground_distance]
        return result

    # Function to calculate ramp-up time and distance
    def ramp_up(CRUISE_SPEED, trip_altitude):
        print("\nInside ramp_up function:")
        print("CRUISE_SPEED:", CRUISE_SPEED)
        print("trip_altitude:", trip_altitude)

        if trip_altitude > 10000:
            initial_speed_kph = 518.56  # kmph (280 knots)
        else:
            initial_speed_kph = 463  # kmph (250 knots)

        # Given data
        final_speed_kph = CRUISE_SPEED
        acceleration_rate_kpm = 46.3  # Acceleration rate in kilometers per minute # kmph (25 knots)

        # Convert acceleration rate to kilometers per hour
        acceleration_rate_kph = acceleration_rate_kpm / 60

        # Calculate ramp up time
        ramp_up_time_minutes = (final_speed_kph - initial_speed_kph) / acceleration_rate_kpm

        # Calculate distance traveled during ramp up
        ramp_up_distance_km = initial_speed_kph * ramp_up_time_minutes/60 + 0.5 * acceleration_rate_kph * ramp_up_time_minutes ** 2

        result = [ramp_up_time_minutes, ramp_up_distance_km]
        return result

    # Function to calculate ramp-down time and distance
    def ramp_down(CRUISE_SPEED, trip_altitude):
        print("\nInside ramp_down function:")
        print("CRUISE_SPEED:", CRUISE_SPEED)
        print("trip_altitude:", trip_altitude)

        # Given data
        if trip_altitude > 10000:
            final_speed_kph = 518.56  # kmph (280 knots)
        else:
            final_speed_kph = 463  # kmph (250 knots)

        # Deceleration rate
        deceleration_rate_kphpm = 35  # Deceleration rate in kilometers per hour per minute

        # Convert deceleration rate to kilometers per minute
        deceleration_rate_kpm = deceleration_rate_kphpm / 60

        # Calculate ramp down time
        ramp_down_time_minutes = (CRUISE_SPEED - final_speed_kph) / deceleration_rate_kphpm

        # Calculate distance traveled during ramp down
        ramp_down_distance_km = (CRUISE_SPEED + final_speed_kph) / 2 * ramp_down_time_minutes / 60  # Average speed * time

        result = [ramp_down_time_minutes, ramp_down_distance_km]
        return result



    # Function to calculate descent time and ground distance
    def descent_time(trip_altitude):
        print("\nInside descent_time function:")
        print("trip_altitude:", trip_altitude)

        time_sum = 0
        descent_distance = 0
        dist_per_1000_feet = 5.556  # km - 3 nautical miles

        if trip_altitude > 10000:
            speed = 463  # kmph (250 knots)
            altitude_to_descend = trip_altitude - 10000  # feet
            descent_distance += (altitude_to_descend / 1000) * dist_per_1000_feet
            time_sum += (descent_distance / speed)*60
            print("descent_distance after first segment:", descent_distance)
            print("time_sum after first segment:", time_sum)

        # starting at 10000 feet - lower speed and descend to 0
        speed = 370.4  # kmph (200 knots)
        descent_distance += (10000 / 1000) * dist_per_1000_feet
        time_sum += (descent_distance / speed)*60
        print("descent_distance after second segment:", descent_distance)
        print("time_sum after second segment:", time_sum)

        ground_distance = descent_distance  # Update to use descent_distance instead of trip_altitude
        result = [time_sum, ground_distance]
        return result


    # Input and output file paths
    airports_csv = '../data/airports.csv'
    weighted_distances_csv = '../data/flight_weighted_distances.csv'

    # Read populations, and airport names from CSV file
    populations = []
    airport_names = []
    with open(airports_csv, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        for row in csv_reader:
            airport_name, metro_pop = row[1], float(row[6])
            populations.append((metro_pop))
            airport_names.append(airport_name)

    print("\nPopulations:", populations)
    print("Airport Names:", airport_names)

    # Read weighted distances from CSV file
    weighted_distances = []
    with open(weighted_distances_csv, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        for row in csv_reader:
            distance_temp = float(row[2])
            weighted_distances.append((distance_temp))

    print("Weighted Distances:", weighted_distances)

    num_points = len(populations)
    k = 0
    time_matrix = [[0.0] * num_points for _ in range(num_points)]
    print("Time Matrix:", time_matrix)

    # Calculate flight times between pairs of airports
    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                time_sum = 0
                origin_population = populations[i]
                origin_airport_name = airport_names[i]
                destination_population = populations[j]
                destination_airport_name = airport_names[j]
                distance = weighted_distances[k]
                trip_altitude = cruising_altitude(distance)
                print("\n Flying from: ", origin_airport_name, "to: ", destination_airport_name, "\n")
                print("Weighted Distance: ", distance)
                print("\n k = ",k)
                # Calculate taxi time before takeoff
                taxi_time_before_takeoff = taxi_time(origin_population, origin_airport_name) + 1
                time_sum += taxi_time_before_takeoff
                print("Taxi time before takeoff:", taxi_time_before_takeoff)
                print("Time sum after taxi time before takeoff:", time_sum)

                # Calculate taxi time before landing
                taxi_time_after_landing = taxi_time(destination_population, destination_airport_name) + 2
                time_sum += taxi_time_after_landing
                print("Taxi time after landing:", taxi_time_after_landing)
                print("Time sum after taxi time after landing:", time_sum)

                # Calculate ascent time and distance
                ascent_result = ascent_time(trip_altitude)
                time_sum += ascent_result[0]
                distance -= ascent_result[1]
                print("Ascent time:", ascent_result[0])
                print("Ascent distance:", ascent_result[1])
                print("Remaining distance after ascent:", distance)
                print("Time sum after ascent time:", time_sum)

                # Calculate descent time and distance
                descent_result = descent_time(trip_altitude)
                time_sum += descent_result[0]
                distance -= descent_result[1]
                print("Descent time:", descent_result[0])
                print("Descent distance:", descent_result[1])
                print("Remaining distance after descent:", distance)
                print("Time sum after descent time:", time_sum)

                # Calculate ramp-up time and distance
                ramp_up_result = ramp_up(CRUISE_SPEED, trip_altitude)
                time_sum += ramp_up_result[0]
                distance -= ramp_up_result[1]
                print("Ramp-up time:", ramp_up_result[0])
                print("Ramp-up distance:", ramp_up_result[1])
                print("Remaining distance after ramp-up:", distance)
                print("Time sum after ramp-up time:", time_sum)

                # Calculate ramp-down time and distance
                ramp_down_result = ramp_down(CRUISE_SPEED, trip_altitude)
                time_sum += ramp_down_result[0]
                distance -= ramp_down_result[1]
                print("Ramp-down time:", ramp_down_result[0])
                print("Ramp-down distance:", ramp_down_result[1])
                print("Remaining distance after ramp-down:", distance)
                print("Time sum after ramp-down time:", time_sum)

                # Calculate time for cruising
                cruising_time = distance / CRUISE_SPEED * 60
                time_sum += cruising_time
                print("Time for cruising:", cruising_time)
                print("Time sum after cruising time:", time_sum)


                # Store the calculated time in the time matrix
                time_matrix[i][j] = time_sum
                k+=1
                print("\n time: ",time_sum)
            else:
                time_matrix[i][j] = -1  # Set diagonal elements to -1

    # Write the distance matrix to a CSV file
    with open(output_csv_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        
        # Write the header row
        csv_writer.writerow(['Origin Airport', 'Destination Airport', 'Flight Time (Minutes)'])
        
        # Write each row with origin airport, destination airport, and corresponding weighted distances
        for i in range(num_points):
            for j in range(num_points):
                if i != j:
                    origin = airport_names[i]
                    destination = airport_names[j]
                    weighted_distance = time_matrix[i][j]
                    # Write the data to the CSV file
                    csv_writer.writerow([origin, destination, weighted_distance])



def extract_aircraft_name(file_name):
    """
    Extracts the aircraft name from the input file name.

    Args:
        file_name (str): The input file name.

    Returns:
        str: The extracted aircraft name.
    """
    # Split the file name by '_' and remove the prefix 'flight_times_'
    aircraft_name = file_name.split('_')[2:]
    # Join the remaining parts and replace underscores with spaces
    return ' '.join(aircraft_name).replace('.csv', '')


def combine_csv_files(output_file, input_files):
    """
    Combines multiple CSV files into one CSV file.

    Args:
        output_file (str): Path to the output CSV file.
        input_files (list of str): Paths to the input CSV files.
    """
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write the header row only once before the loop
        writer.writerow(['Origin Airport', 'Destination Airport', 'Aircraft', 'Flight Time (Minutes)'])
        
        # Initialize the row counter
        row_counter = 0
        
        # Iterate until the end of the files is reached
        while True:
            # Initialize a flag to track if the end of any file is reached
            end_of_any_file = False
            
            # Loop through each input file
            for input_file in input_files:
                # Extract the aircraft name from the file name
                aircraft_name = extract_aircraft_name(os.path.basename(input_file))
                with open(input_file, 'r') as infile:
                    reader = csv.reader(infile)
                    
                    # Skip the header row in the input file
                    next(reader)
                    
                    # Skip rows until reaching the row_counter
                    for _ in range(row_counter):
                        next(reader, None)
                    
                    # Read the next row from the file
                    row = next(reader, None)
                    
                    # If the row is not None, write it to the output file
                    if row is not None:
                        # Reorder the elements in the row
                        reordered_row = [row[0], row[1], aircraft_name, row[2]]
                        
                        # Write the reordered row to the output file
                        writer.writerow(reordered_row)
                        
                    else:
                        # If the row is None, it means the end of the file is reached
                        # Set the flag to True
                        end_of_any_file = True
            
            # If the end of any file is reached, exit the loop
            if end_of_any_file:
                break
            
            # Increment the row counter
            row_counter += 1

# Example usage:
output_combined_csv = "../data/flight_times.csv"
input_files = ['../data/' + name for name in aircraft_names]  # assuming aircraft_names is the list of filenames
combine_csv_files(output_combined_csv, input_files)

# Delete the non-combined files
if (delete_itermediate_files == True):
    for input_file in input_files:
        os.remove(input_file)