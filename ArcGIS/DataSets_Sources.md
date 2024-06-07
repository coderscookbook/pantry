## Dataset Resources
<p>

[Esri Data & Maps](https://www.arcgis.com/home/group.html?id=5c3f279a7ff04e6a96b4ee5acfe778e5)

- Esri provides a collection of ready-to-use datasets that are freely available for ArcGIS users. These datasets include a variety of themes such as demographics, basemaps, boundaries, and more.
</p>

<p>

[Natural Earth Data](https://www.naturalearthdata.com/)

- Natural Earth offers free vector and raster map data at scales suitable for making maps at a global or regional level.

</p>

<p>

[USGS National Map](https://apps.nationalmap.gov/viewer/)

- The USGS provides a wealth of geospatial data, including topographic maps, satellite imagery, and other datasets related to geography and natural resources.

</p>

<p>

[OpenStreetMap Data](https://www.openstreetmap.org/export)
- OpenStreetMap is a collaborative project to create a free editable map of the world. You can download OSM data for various regions and use them in your GIS projects.

</p>

<p>

[NASA Earth Data](https://www.earthdata.nasa.gov/)
- NASA provides access to a wide range of Earth science data, including satellite imagery and other geospatial datasets.

</p>

<p>
<strong>Local Government and Municipal Data Portals</strong>

Many local governments and municipalities provide geospatial data through their data portals. These datasets often include detailed local information like parcels, zoning, infrastructure, and more.

- Example: [NYC Open Data](https://opendata.cityofnewyork.us/)
- Example: [LA GeoHub](https://geohub.lacity.org/)
</p>

## Example Datasets for Testing:
Here are some specific datasets you can use to test examples:

### Natural Earth Data
- Download vector data such as administrative boundaries, populated places, or physical features.
- [Natural Earth Vector Data](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/)

### USGS National Map
- Download datasets such as elevation, hydrography, land cover, or transportation networks.
- [USGS National Map](https://apps.nationalmap.gov/viewer/)

### OpenStreetMap Data
- Download OSM data for specific regions.
- [Geofabrik OSM Data Downloads](https://download.geofabrik.de/)

### Esri Sample Data
- Explore and download sample datasets provided by Esri for various tutorials and exercises.
- [Esri Sample Data](https://www.arcgis.com/home/search.html?q=sample%20data&t=content)

## Download and Use the Data
1. Download the dataset from one of the sources mentioned above.
2. Extract the files if they are compressed (e.g., ZIP files).
3. Place the datasets in a directory on your local machine.
4. Modify the example scripts provided earlier to point to the location of your downloaded datasets.

For example, if you download shapefiles from Natural Earth and place them in C:/path/to/your/geospatial/data, you can use that path in the provided Python scripts for testing.

Here’s a quick example using Natural Earth data for the quadtree decomposition:
```
# Update the directory path to where you extracted the Natural Earth data
root_directory = "C:/path/to/your/geospatial/data/natural_earth_vector"

# Call the process_directory function to start processing the datasets
process_directory(root_directory)
```


