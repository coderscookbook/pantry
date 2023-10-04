
curr_risk_regex = '^(Drought|Flood|Hail|HeatStress|SeaLevelRise|Solar|StormSurge|Tornado|TropicalCyclone|Wildfire|WindGust|WindPower).*2020$'
'''
This is a regular expression used to match strings that start with one of the listed natural disaster types 
(Drought, Flood, Hail, HeatStress, SeaLevelRise, Solar, StormSurge, Tornado, TropicalCyclone, Wildfire, WindGust, WindPower) 
and end with "2020".

Breaking it down:

'^' matches the start of the string
    '(Drought|Flood|Hail|HeatStress|SeaLevelRise|Solar|StormSurge|Tornado|TropicalCyclone|Wildfire|WindGust|WindPower)' 
    is a capture group that matches one of the natural disaster types listed inside the parentheses
'.*' matches any character (except newline) zero or more times
'2020$' matches the literal string "2020" at the end of the string ('$' matches the end of the string)
So, when this regular expression is used in Python code, 
it will match any string that starts with one of the natural disaster types listed and ends with "2020". 

For example, "Flood2020" and "Tornado in 2020" would match, while "2020Flood" and "Tornado in 2021" would not match.
'''

rename_cols = []
for col in curr_risks.columns:
    col_name = col.split('_')[0]
    if(len(re.findall('([A-Z][a-z]+)', col_name)) > 1):
        col_name = '_'.join(re.findall('([A-Z][a-z]+)', col_name))
    rename_cols.append(col_name)

''' 
This code iterates through the column names of a Pandas DataFrame called curr_risks, 
performs some operations on the column names, 
and creates a list of new column names in rename_cols.

Here is a breakdown of the code:

rename_cols = [] initializes an empty list to hold the new column names.

The for loop iterates through each column name in curr_risks.columns.

col.split('_')[0] splits the column name by the underscore character _ 
and takes the first element of the resulting list. 
!!!This removes any text after the first underscore.

The if statement checks if the col_name variable contains more than one capitalized word 
(e.g., "Total_Costs" or "Estimated_Delivery_Date").

If the col_name variable contains more than one capitalized word, re.findall('([A-Z][a-z]+)', 
col_name) uses regular expression to find all capitalized words in the col_name variable. 
This creates a list of capitalized words.

'_'.join(re.findall('([A-Z][a-z]+)', col_name)) joins the capitalized words in the list created in step 5 with underscores between them. 
This creates a new column name that has each capitalized word separated by an underscore.

If the col_name variable does not contain more than one capitalized word, it is left unchanged.

The rename_cols.append(col_name) statement adds the modified or unchanged column name to the rename_cols list.

At the end of the loop, rename_cols contains a list of new column names that have been modified to follow a standardized naming convention. 
This standardized convention appears to involve separating multiple capitalized words with underscores.
'''