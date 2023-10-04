# DESCRIPTION:
'''
The melt() method in Python is a function in the Pandas library 
that is used to transform a DataFrame from a wide format to a long format.

The melt() method essentially unpivots the data, 
which means it takes columns that are in a wide format 
and transforms them into rows in a long format, 
while keeping other columns as identifiers.
'''    

# SYNTAX:
import pandas
pandas.melt(frame, 
            id_vars=None, 
            value_vars=None, 
            var_name=None, 
            value_name='value', 
            col_level=None)

# EXPLANATION:
'''
- frame:    The DataFrame that you want to melt.
- id_vars:  The column(s) in the DataFrame that you want to keep as identifier variables. 
            These columns will not be transformed.
- value_vars: The column(s) in the DataFrame that you want to unpivot.
- var_name:   The name of the column that will contain the column headers of the unpivoted data.
- value_name: The name of the column that will contain the values of the unpivoted data.
- col_level:  If the columns are a MultiIndex, level(s) of the column to use as variable(s).
'''

# USAGE EXAMPLE:
import pandas as pd

df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

melted_df = df.melt(id_vars=['id', 'name'], value_vars=['age'], var_name='variable', value_name='value')

print(melted_df)

# OUTPUT:
'''
   id     name variable  value
0   1    Alice      age     25
1   2      Bob      age     30
2   3  Charlie      age     35

Explanation of Example:
In this example, the id and name columns were specified as identifier variables using the id_vars argument. 
The age column was specified as the column to unpivot using the value_vars argument. 
The resulting DataFrame has a new variable column that contains the name of the unpivoted column (age), 
and a new value column that contains the values from the age column.
'''
# JAVASCRIPT METHOD:
function melt(data, id_vars, value_vars, var_name='variable', value_name='value') {
  const idVarIndices = id_vars.map(col => data.columns.indexOf(col));
  const valueVarIndices = value_vars.map(col => data.columns.indexOf(col));

  const meltedData = [];

  for (let i = 0; i < data.length; i++) {
    const idVars = idVarIndices.map(index => data[i][index]);

    for (let j = 0; j < valueVarIndices.length; j++) {
      const valueVarIndex = valueVarIndices[j];
      const variable = data.columns[valueVarIndex];
      const value = data[i][valueVarIndex];

      meltedData.push(Object.assign({}, ...id_vars.map((col, index) => ({ [col]: idVars[index] })), { [var_name]: variable, [value_name]: value }));
    }
  }

  return meltedData;
}

'''
COMPARE TO PYTHON melt():
const data = [
  { id: 1, name: 'Alice', age: 25 },
  { id: 2, name: 'Bob', age: 30 },
  { id: 3, name: 'Charlie', age: 35 }
];

const id_vars = ['id', 'name'];
const value_vars = ['age'];

const meltedData = melt(data, id_vars, value_vars);

console.log(meltedData);

OUTPUT OF EACH SHOULD BE THE SAME:
[
  { id: 1, name: 'Alice', variable: 'age', value: 25 },
  { id: 2, name: 'Bob', variable: 'age', value: 30 },
  { id: 3, name: 'Charlie', variable: 'age', value: 35 }
]
'''