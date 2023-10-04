# DOCUMENTATION:  
# https://pro.arcgis.com/en/pro-app/latest/arcpy/data-access/updatecursor-class.htm

# SYNTAX:
UpdateCursor(in_table, 
            field_names, 
            {where_clause}, 
            {spatial_reference}, 
            {explode_to_points}, 
            {sql_clause}, 
            {datum_transformation}, 
            {explicit}
            )

# EXAMPLE USAGE:
# (From IRAD line ~223):
with arcpy.da.UpdateCursor(brownfield_spatial_join_lyr, 
                            ['reg_id','brown_test']) as cursor:   
        for row in cursor:
            if (row[0]): 
                row[1] = 1
            else:
                row[1] = 0
            cursor.updateRow(row)     

# EXPLANATION:
'''
Line1: 
    adds a new field named 'brown_test' to FL brownfield_spatial_join_lyr
    field type is long, can store integers
as cursor: 
    creates and update cursor for the FL with two fields
    used to update values of the 'brown_test' field
for row in cursor: 
    loops through each row in the FL
if (row[0]):
    checks if the 'reg_id' attribute in the current row exists
        is not NONE or empty
        if it does exist, value of 'brown_test' = 1
    else
        if reg_id does not exist, 'brown_test' = 0
cursor.updateRow(row):
    updates 'brown_test' field with the new value
'''