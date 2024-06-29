# Allows us to combine expressions and assignments
# EXAMPLE 1:
if __name__ == '__main__':
    text = 'This is a very long sentence.'

    # Regular Way:
    # words = text.split()
    #info = {
    #    "words": words
    #}
    info = { 
        'words': (words := text.split()),
        'characters': (chars := len("".join(words))),
        'avg_char_per_word': round(chars / len(words), 2)
    }    
    
    print(info)
    
# EXAMPLE 2: use a variable if it exists
name = 'Mario'
empty_name = ''

# expression works if value on right of walrus is true
if temp_name := empty_name or name:
        print(temp_name)
        print('Executed')  
        
########################################################################################
# GEOPROCESSING EXAMPLE 1: 
# - Calculate total distance covered by a list of sequential waypoints (lat, lon)
########################################################################################
from math import radians, sin, cos, sqrt, atan2

# Function to calculate the distance between two geographical points using the Haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = R * c
    return distance

# List of waypoints (latitude, longitude)
waypoints = [
    (34.0522, -118.2437),  # Los Angeles
    (36.1699, -115.1398),  # Las Vegas
    (40.7128, -74.0060),   # New York
    (37.7749, -122.4194)   # San Francisco
]

# Calculate the total distance covered by the waypoints
total_distance = 0
for i in range(len(waypoints) - 1):
    total_distance += calculate_distance(
        waypoints[i][0], waypoints[i][1],
        waypoints[i + 1][0], waypoints[i + 1][1]
    )

print(f"Total distance without walrus operator: {total_distance:.2f} km")

# Now using the walrus operator to simplify the loop
total_distance = 0
i = 0
while i < len(waypoints) - 1:
    total_distance += (dist := calculate_distance(
        waypoints[i][0], waypoints[i][1],
        waypoints[i + 1][0], waypoints[i + 1][1]
    ))
    print(f"Distance between waypoint {i} and {i+1}: {dist:.2f} km")
    i += 1

print(f"Total distance with walrus operator: {total_distance:.2f} km")

########################################################################################
# GEOPROCESSING EXAMPLE 2:
# - iterating oer feature classes in a workspace, calculating the area of each polygon 
# - feature, and storing the total area for each feature class
########################################################################################
import arcpy

# Set the workspace
arcpy.env.workspace = "C:/path/to/your/workspace"

# List all feature classes in the workspace
feature_classes = arcpy.ListFeatureClasses()

# Dictionary to store total area for each feature class
total_areas = {}

for fc in feature_classes:
    total_area = 0
    with arcpy.da.SearchCursor(fc, ["SHAPE@AREA"]) as cursor:
        for row in cursor:
            # Use the walrus operator to accumulate the total area
            total_area += (area := row[0])
    total_areas[fc] = total_area

# Print the total areas
for fc, area in total_areas.items():
    print(f"Total area for {fc}: {area} square units")

################################################################ VERSION 2
import arcpy
import numpy as np

# Set the workspace
arcpy.env.workspace = "C:/path/to/your/workspace"

# List all feature classes in the workspace
feature_classes = arcpy.ListFeatureClasses()

# Dictionary to store total area for each feature class
total_areas = {}

for fc in feature_classes:
    # Convert the feature class to a NumPy array
    array = arcpy.da.FeatureClassToNumPyArray(fc, ["SHAPE@AREA"])
    
    # Use NumPy operations to calculate the total area
    total_area = 0
    for area in array["SHAPE@AREA"]:
        total_area += area  # Using the walrus operator isn't necessary here since we're not filtering or transforming
    
    total_areas[fc] = total_area

# Print the total areas
for fc, area in total_areas.items():
    print(f"Total area for {fc}: {area} square units")