import math
import csv

radius_of_earth = 6378.14  


def haversine_distance(lat1, lon1, lat2, lon2):
    phi_A, lambda_A, phi_B, lambda_B = map(math.radians, [lat1, lon1, lat2, lon2])
    distance = radius_of_earth * math.acos(math.sin(phi_A) * math.sin(phi_B) + math.cos(phi_A) * math.cos(phi_B) * math.cos(lambda_A - lambda_B))
    if distance < 242:
        distance = -1
    return distance


def wdistance(lat1, lon1, lat2, lon2):
    distance = haversine_distance(lat1, lon1, lat2, lon2)
    if distance < 0:
        return distance
    
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

    if angle <= 90:
        percentage = angle / 90
    else:
        percentage = (angle - 90) / 90

    print("\nlat1 = ", lat1,
          "\nlat2 = ", lat2,
          "\ndeltaLat: ", deltaLat,
          "\nlon1 = ", lon1,
          "\nlon2 = ", lon2,
          "\ndeltaLon: ", deltaLon,
          "\nDistance: ", distance,
          "\nAngle: ", angle,
          "\nPercentage: ", percentage)

    # Adjust weighted distance based on direction
    if deltaLon > 0:  # Going West - flight time increases
        weightedDistance = distance + (distance * 0.045 * percentage)
    elif deltaLon < 0:  # Going East - flight time decreases
        weightedDistance = distance + (distance * -0.045 * percentage)
    else:  # Going exactly north or south
        weightedDistance = distance

    print("\nDistance: ", distance,
          "\nWeighted Distance: ", weightedDistance,
          "\n")

    return weightedDistance

csv_file_path = 'airports.csv'
output_csv_path = 'weighted_distances.csv'

# Read latitude and longitude from CSV file
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
            distance_matrix[i][j] = wdistance(lat1, lon1, lat2, lon2)
        else:
            distance_matrix[i][j] = -1

# Write the distance matrix to a CSV file
with open(output_csv_path, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    
    # Write the header row
    csv_writer.writerow([''] + airport_names)
    
    # Write each row with airport name and corresponding distances
    for i in range(num_points):
        row_data = [airport_names[i]] + distance_matrix[i]
        csv_writer.writerow(row_data)
