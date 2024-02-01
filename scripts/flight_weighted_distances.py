"""
AUTHOR: Corey Lawrence

Script to calculate weighted distances between pairs of airports considering the direction of travel.

This script reads airport data from a CSV file containing latitude and longitude information.
It then calculates the distances between all pairs of airports using the Haversine formula
and adjusts these distances based on the direction of travel. The resulting weighted distances
are stored in a CSV file with columns for the origin airport, destination airport, and the
calculated weighted distance.

Functions:
    - haversine_distance(lat1, lon1, lat2, lon2): Calculates the Haversine distance between two points.
    - wdistance(lat1, lon1, lat2, lon2): Calculates the weighted distance between two points.

Input:
    - 'airports.csv': CSV file containing airport data including latitude and longitude.
Output:
    - 'flight_weighted_distances.csv': CSV file containing the weighted distances between pairs of airports.
"""

import math
import csv

# Radius of the Earth in kilometers
radius_of_earth = 6378.14  

# Function to calculate the Haversine distance between two points given their latitudes and longitudes
def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    phi_A, lambda_A, phi_B, lambda_B = map(math.radians, [lat1, lon1, lat2, lon2])
    # Calculate the distance using Haversine formula
    distance = radius_of_earth * math.acos(math.sin(phi_A) * math.sin(phi_B) + math.cos(phi_A) * math.cos(phi_B) * math.cos(lambda_A - lambda_B))
    # If the distance is less than 242 km, set it to -1
    if distance < 242:
        distance = -1
    return distance

# Function to calculate the weighted distance between two points considering the direction of travel
def wdistance(lat1, lon1, lat2, lon2):
    distance = haversine_distance(lat1, lon1, lat2, lon2)
    if distance < 0:
        return distance
    
    # Calculate the difference in latitudes and longitudes
    deltaLat = lat2 - lat1
    deltaLon = lon2 - lon1

    lat1Rad = math.radians(lat1)
    lat2Rad = math.radians(lat2)
    lon1Rad = math.radians(lon1)
    lon2Rad = math.radians(lon2)

    # Calculate the components of the vectors
    x1 = math.cos(lat1Rad) * math.cos(lon1Rad)
    y1 = math.cos(lat1Rad) * math.sin(lon1Rad)
    z1 = math.sin(lat1Rad)

    x2 = math.cos(lat2Rad) * math.cos(lon2Rad)
    y2 = math.cos(lat2Rad) * math.sin(lon2Rad)
    z2 = math.sin(lat2Rad)

    # Calculate the dot product of the two vectors
    dot_product = x1 * x2 + y1 * y2 + z1 * z2

    # Calculate the angle between the two vectors
    angle = math.degrees(math.acos(dot_product))

    # Calculate the percentage of angle
    if angle <= 90:
        percentage = angle / 90
    else:
        percentage = (angle - 90) / 90

    # Adjust weighted distance based on direction of travel
    if deltaLon > 0:  # Going West - flight time increases
        weightedDistance = distance + (distance * 0.045 * percentage)
    elif deltaLon < 0:  # Going East - flight time decreases
        weightedDistance = distance + (distance * -0.045 * percentage)
    else:  # Going exactly north or south
        weightedDistance = distance

    return weightedDistance

# Input and output file paths
csv_file_path = 'data/airports.csv'
output_csv_path = 'data/flight_weighted_distances.csv'

# Read latitude, longitude, and airport names from CSV file
coordinates = []
airport_names = []
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        latitude, longitude, airport_name = float(row[7]), float(row[8]), row[1]
        coordinates.append((latitude, longitude))
        airport_names.append(airport_name)

# Calculate distances and store in a matrix
num_points = len(coordinates)
distance_matrix = [[0.0] * num_points for _ in range(num_points)]

for i in range(num_points):
    for j in range(num_points):
        if i != j:
            lat1, lon1 = coordinates[i]
            lat2, lon2 = coordinates[j]
            # Calculate weighted distance between each pair of airports
            distance_matrix[i][j] = wdistance(lat1, lon1, lat2, lon2)
        else:
            distance_matrix[i][j] = -1  # Set diagonal elements to -1

# Write the distance matrix to a CSV file
with open(output_csv_path, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    
    # Write the header row
    csv_writer.writerow(['Origin Airport', 'Destination Airport', 'Weighted Distance'])
    
    # Write each row with origin airport, destination airport, and corresponding weighted distances
    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                origin = airport_names[i]
                destination = airport_names[j]
                weighted_distance = distance_matrix[i][j]
                # Write the data to the CSV file
                csv_writer.writerow([origin, destination, weighted_distance])
