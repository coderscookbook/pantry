# list_methods.py
my_list = [['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one']]
my_other_list = ["b",1,2,3,4,6,7,8,9,10]
# append()
my_list.append(['zero'])
print(f"append: {my_list}")

# extend()
my_list.extend(['negative one', 'negative two'])
print(f"extend: {my_list}")

# insert()
my_list.insert(0, ['eleven'])
print(f"insert: {my_list}")

# remove()
my_list.remove(['ten'])
print(f"remove: {my_list}")

# pop()
my_list.pop(0)
print(f"pop: {my_list}")

# index()
index = my_list.index(['nine'])
print(f"index: {index}")

# count()
count = my_list.count(['nine'])
print(f"count: {count}")

# sort()
my_list.sort()
print(f"sort: {my_list}")

# reverse()
my_list.reverse()
print(f"reverse: {my_list}")

# slice notation
num = 5 
char = 'm'
my_other_list[3:3] = num # error
my_other_list[3:3] = char
print(my_other_list)