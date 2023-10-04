# combining_data_types.py
# Combining Lists, Dictionaries, and Tuples

# You can use lists, dictionaries, and tuples together in many different ways to organize and manipulate data.

# For example, you can create a list of dictionaries to represent a table of data:
table = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 40},
    {'name': 'Charlie', 'age': 50}
]

# You can access the data in the table using indexing and key-value pairs:
print(f"Alice's age: {table[0]['age']}")

# You can also use a list of tuples to represent a table of data:
table = [
    ('Alice', 30),
    ('Bob', 40),
    ('Charlie', 50)
]

# You can access the data in the table using indexing and tuple unpacking:
name, age = table[0]
print(f"Alice's age: {age}")

# You can use a dictionary with tuple keys to represent a sparse matrix:
matrix = {
    (0, 0): 1,
    (0, 1): 2,
    (1, 0): 3,
    (1, 1): 4
}

# You can access the data in the matrix using key-value pairs:
print(f"Value at (0, 0): {matrix[(0, 0)]}")

# You can use a list of lists to represent a matrix:
matrix = [
    [1, 2],
    [3, 4]
]

# You can access the data in the matrix using indexing:
print(f"Value at (0, 0): {matrix[0][0]}")

# These are just a few examples of how you can combine lists, dictionaries, and tuples to organize and manipulate data in dynamic ways.