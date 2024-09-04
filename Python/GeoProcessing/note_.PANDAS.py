# Pandas DataFrames talking about example in L21 note_regex.py
# https://www.w3schools.com/python/pandas/pandas_dataframes.asp

# CREATE FEATURE CLASS/SHAPEFILE from CSV
import arcpy
import pandas as pd

# Define paths
csv_file = 'arcgis_data.csv'
gdb = 'path_to_your_geodatabase.gdb'
feature_class_name = 'arcgis_data'

# Create a spatial reference (e.g., WGS 84)
spatial_reference = arcpy.SpatialReference(4326)

# Create feature class in geodatabase
arcpy.CreateFeatureclass_management(out_path=gdb, out_name=feature_class_name, 
                                     geometry_type="POINT", spatial_reference=spatial_reference)

# Define fields for feature class
fields = ['ID', 'Name', 'Latitude', 'Longitude', 'LandUse', 'Area_sq_km', 'Population', 'Elevation_m']

# Add fields to the feature class
for field in fields:
    if field not in ['Latitude', 'Longitude']:
        arcpy.AddField_management(f"{gdb}/{feature_class_name}", field, "TEXT")

# Add Latitude and Longitude fields as double
arcpy.AddField_management(f"{gdb}/{feature_class_name}", 'Latitude', "DOUBLE")
arcpy.AddField_management(f"{gdb}/{feature_class_name}", 'Longitude', "DOUBLE")

# Insert data into the feature class
with arcpy.da.InsertCursor(f"{gdb}/{feature_class_name}", fields) as cursor:
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        point = arcpy.Point(row['Longitude'], row['Latitude'])
        cursor.insertRow((row['ID'], row['Name'], row['Latitude'], row['Longitude'], row['LandUse'], row['Area_sq_km'], row['Population'], row['Elevation_m']))

print("Feature class created successfully.")


# WITHOUT ARCPY
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

# Create a DataFrame with your data
data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Location1', 'Location2', 'Location3', 'Location4', 'Location5'],
    'Latitude': [34.05, 36.16, 37.77, 40.71, 41.88],
    'Longitude': [-118.24, -115.15, -122.41, -74.01, -87.63],
    'LandUse': ['Residential', 'Commercial', 'Industrial', 'Park', 'Agricultural'],
    'Area_sq_km': [10.0, 20.0, 15.0, 5.0, 25.0],
    'Population': [1000, 5000, 2000, 3000, 4000],
    'Elevation_m': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)

# Convert DataFrame to GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))

# Define a coordinate reference system (CRS)
gdf.crs = "EPSG:4326"  # WGS 84

# Save the GeoDataFrame to a shapefile
gdf.to_file('arcgis_data.shp')

print("Shapefile created successfully.")
