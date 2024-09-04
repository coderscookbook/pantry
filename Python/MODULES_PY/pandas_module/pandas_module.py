import pandas as pd

data = {"one": 1, "two": 2, "three": 3, "four": 4}
print("\ndata: \n", data)

# Explicitly providing an index
df = pd.DataFrame(data, index=["a", "b", "c", "d"])
print("\nExplicit Index: \n", df)
''' OUTPUT:
   one  two  three  four
a    1    2      3     4
b    1    2      3     4
c    1    2      3     4
d    1    2      3     4
'''
# Turning dictionary into a list of lists
data_list = [[key, value] for key, value in data.items()]
print("\ndata_list: \n", data_list)

# Implicitly providing an index using a list of lists
# data_list = [["one", 1], ["two", 2], ["three", 3], ["four", 4]]
df = pd.DataFrame(data_list, columns=["word", "symbol"])
print("\nImplicit Index: \n", df)
''' OUTPUT:
    word  symbol
0    one       1
1    two       2
2  three       3
3   four       4
'''
