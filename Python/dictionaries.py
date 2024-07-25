''' 
NOTES: 
- dictionaries are not very fast if you don't know the value in the key-value
  pair you're looking for
- work best when value of key-value pair is known
- aka Map, Key-Value Store, Hashmap
- just like lists, dicts live in the heap

IMPORTANT:
- cannot have duplicate keys
- can have duplicate values

'''

'''Demonstrations of dictionary capabilities'''
# Declaring/define the type of a dictionary
schools: dict[str, int]
# students: dict[list[str, int]]

# Initialize/construct to an empty dictionary//assign reference to the dictionary
schools = dict()

# Set a key-value pairing in the dictionary
# Unlike lists, append method not used
schools["UNC"]  = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation 
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools["UNC"]} students")

# Remove a key-value pair from dictionary by its key
# schools.pop("Duke")
# del my_dict["Duke"]

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")
print(schools)

# Update/reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200
schools["Duke"] = schools["Duke"] + 400       #if "Duke" not removed
print(schools)

# Invert values (switched key with values): but doesn't make sense for this case
invert_schools: dict[int, str]
invert_schools[19400] = "UNC"

########################################################################
# Iterating
########################################################################
for school in schools:
  print(school, schools[school])

for value in schools.values():
  print(value)
  
for school, value in schools.items():
  print(school, value)


########################################################################
# Demonstration of dictionary literals
########################################################################
# Empty dictionary literal
schools = {}  # same as dict()
print(schools)

# Altnernatively, initialize key-value paris
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

########################################################################
# Dictionary methods
########################################################################
# clear()
# copy()
# fromkeys()
# get()
# items()
# keys()
# pop()
# popitem()
# setdefault()
# update()
# values()

