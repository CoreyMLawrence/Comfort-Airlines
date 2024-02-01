"""
AUTHOR: Corey Lawrence

Script to calculate the distances between pairs of airports using the Haversine formula.

This script reads airport data from a CSV file containing latitude and longitude information.
It then calculates the distances between all pairs of airports using the Haversine formula,
which considers the curvature of the Earth. The distances are stored in a CSV file with
columns for the origin airport, destination airport, and the calculated distance.

Input:
    - 'airports.csv': CSV file containing airport data including latitude and longitude.
Output:
    - 'distances.csv': CSV file containing the distances between pairs of airports.
"""

import math
import csv

# Function to calculate the Haversine distance between two points given their latitudes, longitudes, and radius
def haversine_distance(lat1, lon1, lat2, lon2, radius):
    # Convert degrees to radians
    phi_A, lambda_A, phi_B, lambda_B = map(math.radians, [lat1, lon1, lat2, lon2])
    # Calculate the distance using Haversine formula
    distance = radius * math.acos(math.sin(phi_A) * math.sin(phi_B) + math.cos(phi_A) * math.cos(phi_B) * math.cos(lambda_A - lambda_B))
    # If the distance is less than 242 km, set it to -1
    if distance < 242:
        distance = -1
    return distance

# Input and output file paths
csv_file_path = 'airports.csv'
output_csv_path = 'distances.csv'
radius_of_earth = 6378.14  

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

# Calculate distances and store in a list
distances = []

# Populate the distances list
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            lat1, lon1 = coordinates[i]
            lat2, lon2 = coordinates[j]
            # Calculate Haversine distance between each pair of airports
            distance = haversine_distance(lat1, lon1, lat2, lon2, radius_of_earth)
            # Append origin airport, destination airport, and distance to the distances list
            distances.append([airport_names[i], airport_names[j], distance])

# Write the distances list to a CSV file
with open(output_csv_path, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    
    # Write the header row
    csv_writer.writerow(['Origin Airport', 'Destination Airport', 'Distance'])
    
    # Write each row with origin airport, destination airport, and corresponding distance
    for row_data in distances:
        csv_writer.writerow(row_data)
