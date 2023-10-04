'''
SOURCE: https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-field.htm

SUMMARY:
create a new field called MyNewField in the feature class MyFeatureClass. The field will be a text field with a precision of 10, a scale of 2, and a length of 20. The field will be nullable and non-required.

Here is a breakdown of what each line of code does:

import arcpy:           This imports the arcpy module, which contains all of the ArcGIS functionality for Python.
arcpy.env.workspace =   "C:/Users/YourUserName/Documents/ArcGIS/Default.gdb": This sets the workspace to the current user's Documents folder.
fc =                    "MyFeatureClass": This creates a variable called fc and assigns it the value of the feature class name.
field =                 arcpy.AddField_management(fc, "MyNewField", "TEXT", "", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""): This calls the AddField_management function to create a new field. The function takes the following arguments:
fc:                     The feature class where the new field will be created.
MyNewField:             The name of the new field.
TEXT:                   The data type of the new field.
precision:              The precision of the new field.
scale:                  The scale of the new field.
length:                 The length of the new field.
alias:                  The alias of the new field.
nullable:               A Boolean value that specifies whether the field can be null.
required:               A Boolean value that specifies whether the field is required.
field.precision = 10:   This sets the precision of the field to 10.
field.scale = 2:        This sets the scale of the field to 2.
field.length = 20:      This sets the length of the field to 20.
field.update():         This updates the field with the new properties.
'''

# CODE:

import arcpy

# Set the workspace
arcpy.env.workspace = "C:/Users/YourUserName/Documents/ArcGIS/Default.gdb"

# Get the feature class
fc = "MyFeatureClass"

# Create a new field
field = arcpy.AddField_management(fc, "MyNewField", "TEXT", "", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Set the field properties
field.precision = 10
field.scale = 2
field.length = 20

# Update the field
field.update()