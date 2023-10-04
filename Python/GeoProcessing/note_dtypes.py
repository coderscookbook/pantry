'''
In Python, the .dtypes attribute is used to display the data type of each column in a Pandas DataFrame or Series object.
Pandas is a popular library for data manipulation and analysis in Python, 
and it provides a number of useful functions and methods for working with tabular data.

The .dtypes attribute returns a Series object that contains the data type of each column in the DataFrame or Series. 
The index of the Series corresponds to the column names, and the values of the Series correspond to the data types of each column.
'''

# For example, consider the following Pandas DataFrame:

import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'gender': ['female', 'male', 'male']}

df = pd.DataFrame(data)

# Calling df.dtypes on this DataFrame would return the following:

name    == object
age     == int64
gender  == object
dtype: object

'''
This tells us that the name and gender columns are of type object, which typically means they contain strings, and the age column is of type int64, which means it contains integer values.

Knowing the data types of each column in a DataFrame can be helpful for a number of tasks, such as:

Identifying potential data type mismatches or inconsistencies in the data
Converting data types to more appropriate types (e.g., converting a string column to a datetime column)
Filtering or selecting columns based on their data types.
'''

import pandas as pd

data = {'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'score': [95.0, 80.5, 75.0]}

df = pd.DataFrame(data)

print(df.dtypes)

# Returns
id         int64
name      object
score    float64
dtype: object

