# instantiate dictionary
my_dict = {'10': 'a', '9':'b', '8':'c', '7':'d', '6':'e','5':'f'}

# keys()
keys = my_dict.keys()
print(f"keys: {keys}")        # dict_keys(['10', '9', '8', '7', '6', '5'])

# values()
values = my_dict.values()
print(f"values: {values}")    # dict_values(['a', 'b', 'c', 'd', 'e', 'f'])

# items()
items = my_dict.items()
print(f"items: {items}")      # [('10', 'a'), ('9', 'b'), ('8', 'c'), ('7', 'd'), ('6', 'e'), ('5', 'f')]

# get()
value = my_dict.get('10')
print(f"get: {value}")        # a

# update()
my_dict.update({'4': 'g'})
print(f"update: {my_dict}")   # {'10': 'a', '9': 'b', '8': 'c', '7': 'd', '6': 'e', '5': 'f', '4': 'g'} 

# popitem()
my_dict.popitem()
print(f"popitem: {my_dict}")  # {'10': 'a', '9': 'b', '8': 'c', '7': 'd', '6': 'e'}

# pop()
my_dict.pop('10')
print(f"pop: {my_dict}")      # {'9': 'b', '8': 'c', '7': 'd', '6': 'e'}