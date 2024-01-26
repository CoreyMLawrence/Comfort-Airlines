import math
import csv

def haversine_distance(lat1, lon1, lat2, lon2, radius):
    phi_A, lambda_A, phi_B, lambda_B = map(math.radians, [lat1, lon1, lat2, lon2])
    distance = radius * math.acos(math.sin(phi_A) * math.sin(phi_B) + math.cos(phi_A) * math.cos(phi_B) * math.cos(lambda_A - lambda_B))
    if distance < 242:
        distance = -1
    return distance

csv_file_path = 'airports.csv'
output_csv_path = 'distance_matrix.csv'
radius_of_earth = 6378.14  

# Read latitude and longitude from CSV file
coordinates = []
airport_names = []
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        latitude, longitude, airport_name = float(row[6]), float(row[7]), row[1]
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
            distance_matrix[i][j] = haversine_distance(lat1, lon1, lat2, lon2, radius_of_earth)

# Write the distance matrix to a CSV file
with open(output_csv_path, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    
    # Write the header row
    csv_writer.writerow([''] + airport_names)
    
    # Write each row with airport name and corresponding distances
    for i in range(num_points):
        row_data = [airport_names[i]] + distance_matrix[i]
        csv_writer.writerow(row_data)
