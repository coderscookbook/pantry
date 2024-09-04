import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import os

# Create a DataFrame with your data
cwd       = os.getcwd()
filepath  = os.path.join(cwd, 'geo_data.csv')

df        = pd.read_csv(filepath)
df        = pd.DataFrame(df)

# One Line:
# gdf       = gpd.GeoDataFrame(
#               df,
#               geometry=gpd.points_from_xy(df.Longitude, df.Latitude),
#               crs="EPSG: 4326"
#             )

# Convert DataFrame to GeoDataFrame
gdf = gpd.GeoDataFrame( 
                        df, 
                        geometry=gpd.points_from_xy(df.Longitude, df.Latitude)
                      )

# Define a coordinate reference system (CRS)
gdf.crs = "EPSG:4326"  # WGS 84

# Save the GeoDataFrame to a shapefile
gdf.to_file('arcgis_data.shp')

# print(gdf)
print("Shapefile created successfully.")
