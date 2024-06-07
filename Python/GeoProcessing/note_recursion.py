# RECURSION in GEOPROCESSING/GEOSERVICES
'''
1. Recursive Directory Traversal:
    - when dealing with nested directories of geospatial files
2. Recursive Spatial Analysis:
    - when performing operations that requre subdividing a spatial extent
    - e.g. quadtree decomposition, recursive tiling for raster processing
3. Nested Feature Exploration:
    - when working w/nested geospatial features such as hierarchical data 
        structures in GIS (e.g. regions containing subregions)
4. Automating Batch Processing:
    - when you need to apply the same processing steps to a collection of 
        datasets organized in a hierarchical manner
'''


#####################################################################################
# EXAMPLE 1 (GEOPROCESSING/AUTOMATE BATCH PROCESSING): Recursive Directory Traversal# 
#                                                      for                          #
#                                                      Processing Geospatial Files/ #
#                                                      Processing Multiple Datasets #                                    
#####################################################################################
'''
Let's say you have a directory structure with multiple subdirectories, each containing various geospatial files (like shapefiles, GeoJSON, or rasters). You need to process each file in all subdirectories. Recursion is an ideal solution for this task because it allows you to explore each directory and its subdirectories systematically.
'''

#Recursive Function to Process Geospatial Files
# - recursively list and process all shapefiles in a directory and its subdirectories
import os
import arcpy

def ProcessShapefile(shapefile_path):
    # Example Processing: Describe the shapefile and print its spatial reference
    shp_desc = arcpy.Describe(shapefile_path)
    print(f"Processing {shapefile_path}")
    print(f"Spatial Reference: {shp_desc.spatialReference.name}")

def ProcessDirectory(directory_path):
    # Create path strings for all items in directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            # If the item is a directory, recurse into it
            ProcessDirectory(item_path)                         ### RECURSION ###
        elif item_path.endswith(".shp"):
            # If the item is a shapefile, process it
            ProcessShapefile(item_path)

# Example Usage
root_directory = "~"
ProcessDirectory(root_directory)



#####################################################################################
# EXAMPLE 2 (GEOSERVICES): Recursive Spatial Analysis with Quadtrees                #
#####################################################################################
'''
Implementing quadtree spacial index. Quadtrees are used to recursively subdivide a 2D space into four quadrants or regions, making them useful for tasks like spatial indexing, clustering, or efficient queries.
- example demostrates how recursion is used to subdivide the spatial extent and then insert points into the appropriate quadrant
- Subdivide() and Insert() methods use recursion to handle the hierarchical structure of the quadtree
'''

class Quadtree:
    def __init__(self, bounds, depth=0, max_depth=4):
        self.bounds     = bounds        # xmin, ymin, xmax, ymax
        self.depth      = depth
        self.max_depth  = max_depth
        self.points     = []
        self.children   = []

    def Subdivide(self):
        xmin, ymin, xmax, ymax = self.bounds
        midx = (xmin + xmax) / 2
        midy = (ymin + ymax) / 2
        self.children = [
            Quadtree((xmin, ymin, midx, midy), self.depth + 1, self.max_depth),
            Quadtree((midx, ymin, xmax, midy), self.depth + 1, self.max_depth),
            Quadtree((xmin, midy, midx, ymax), self.depth + 1, self.max_depth),
            Quadtree((midx, midy, xmax, ymax), self.depth + 1, self.max_depth),
        ]

    def Insert(self, point):
        if self.depth == self.max_depth:
            self.points.append(point)
        else:
            if not self.children:
                self.Subdivide()
            for child in self.children:
                if child.Contains(point):
                    child.Insert(point)
                    break

    def Contains(self, point):
        xmin, ymin, xmax, ymax = self.bounds
        x, y = point
        return xmin <= x < xmax and ymin <= y < ymax

# Example Usage
root_bounds = (0, 0, 100, 100)
quadtree    = Quadtree(root_bounds)
# Insert Some Points
points = [(10, 10), (50, 50), (70, 70), (90, 90)]
for point in points:
    quadtree.Insert(point)



#####################################################################################
# EXAMPLE 3 (FEATURES): NEsted Feature Exploration - Hierarchical Regions           #
#####################################################################################
'''
'''
import arcpy
def ProcessRegion(feature_class, region_id):
    # Select region by ID
    where_clause = f"RegionID = {region_id}"
    arcpy.MakeFeatureLayer_management(feature_class, "region_lyr", where_clause)
    
    # Process region (example: print the region's name)
    with arcpy.da.SearchCursor("region_lyr", ["RegionName"]) as cursor:
        for row in cursor:
            print(f"Processing region: {row[0]}")

    # Get Subregions
    subregion_fc = "Subregions"
    subregion_where_clause = f"ParentRegionId = {region_id}"
    arcpy.MakeFeatureLayer_management(subregion_fc, "subregion_lyr", subregion_where_clause)
    
    with arcpy.da.SearchCursor("subregion_lyr", ["SubregionID"]) as cursor:
        for row in cursor:
            subregion_id = row[0]
            process_region(subregion_fc, subregion_id)              # Recursively process subregion

# Example usage
root_region_fc  = "Regions"
root_region_id  = 1
ProcessRegion(root_region_fc, root_region_id)

