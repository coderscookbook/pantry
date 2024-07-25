# instantiate dictionary
my_dictB: dict = {'10': 'a', '9':'b', '8':'c', '7':'d', '6':'e','5':'f'}

# keys()
keys = my_dictB.keys()
print(f"keys: {keys}")        # dict_keys(['10', '9', '8', '7', '6', '5'])

# values()
values = my_dictB.values()
print(f"values: {values}")    # dict_values(['a', 'b', 'c', 'd', 'e', 'f'])

# items(): returns an iterable that contains tuple of key and value pair
items = my_dictB.items()
print(f"items: {items}")      # [('10', 'a'), ('9', 'b'), ('8', 'c'), ('7', 'd'), ('6', 'e'), ('5', 'f')]
for k,v in my_dictB.items():
  print(k,v)

# get(): gets a value without raising an exception - returns NONE
value = my_dictB.get('10')
print(f"get: {value}")        # a
print(my_dictB.get('10'))     # a
print(my_dictB.get(999))      # None
print(my_dictB.get(999, "Missing!")) # Missing!

# update(): expand dictionary, adding same key replaces existing key, use |(union) to append dictionary
my_dictB.update({'4': 'g'})
print(f"update: {my_dictB}")   # {'10': 'a', '9': 'b', '8': 'c', '7': 'd', '6': 'e', '5': 'f', '4': 'g'} 
print(my_dictB | {'1': 'Spam', '2': 'eggs'})
my_dictB |= {'100': 'Fried', '99': 'Chicken'}
print(my_dictB)

# popitem()
my_dictB.popitem()
print(f"popitem: {my_dictB}")  # {'10': 'a', '9': 'b', '8': 'c', '7': 'd', '6': 'e'}

# pop(): needs a key value
my_dictB.pop('10')
popped: str = my_dictB.pop('9')
print(f"pop: {my_dictB}")      # {'9': 'b', '8': 'c', '7': 'd', '6': 'e'}
print(f"popped: {popped}")     # b

# popitem(): pops last item from dictionary
my_dictB.popitem()
print(my_dictB)

# copy(): creates shallow copy, diff memory locations
sample_dict: dict = {0: ['a', 'b'], 1: ['c', 'd']}
my_copy: dict = sample_dict.copy()
print(id(sample_dict))
print(id(my_copy))

my_copy[0][0] = "!!!"         # changes both due to shallow coppying, to prevent - use deep copying
print(sample_dict)
print(my_copy)
sample_dict[1][1] = "$$$"
print(sample_dict)
print(my_copy)


# setdefault(): tries to find key value pair, but creates if doesn't exist
users: dict = {0: 'Mario', 2: 'Luigi', 3: 'Peach'}
print(users.setdefault(0, '???'))
print(users.setdefault(999, '???'))
print(users)

# clear(): clears the dictionary, removes everything
users.clear()

# fromkeys(): 
usersB: dict = {0: 'Mario', 2: 'Luigi', 3: 'Peach'}
new_users: dict = dict.fromkeys(usersB)
print(new_users)

usersC: dict = dict.fromkeys(usersB, 'Unknown')
print(usersC)

