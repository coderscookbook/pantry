######################################################################################
# 1. Lists: ordered, mutable, hold elements of different data types
######################################################################################
# Create a List
my_list = [1, 2, 3, "hello", True]
# Accessing elements 
print(my_list[0])       # 1
print(my_list[3])       # hello
# Modifying elements
my_list[1] = "world"
print(my_list)          # [1, 'world', 3, 'hello', True]
# Appending elements
my_list.append(4)
print(my_list)          # [1, 'world', 3, 'hello', True, 4]
# Removing elements
my_list.remove("world")
print(my_list)          # [1, 3, 'hello', True, 4]

######################################################################################
# 2. Tuples: similar to list BUT immutable
######################################################################################
# Create a tuple
my_tuple = (1, 2, 3, "hello", True)
# Accessing elements
print(my_tuple[0])      # 1
# NOTE: attempting to modify a tuple will raise an error
my_tuple[1] = "world"   # TypeError: 'tuple' object does not support item assignment

######################################################################################
# 3. Dictionaries: unordered collections of key-value pairs; allow fast lookup and retrieval of values
######################################################################################
# Create a dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}
# Accessing values
print(my_dict["name"])  # John
print(my_dict["age"])   # 25
# Modifying values
my_dict["age"] = 26
print(my_dict["age"])   # 26
# Adding new key-value pairs
my_dict["country"] = "USA"
print(my_dict)          # {'name': 'John', 'age': 26, 'city': 'New York', 'country': 'USA'}
# Removing key-value pairs
del my_dict["age"]
print(my_dict)          # {'name': 'John', 'city': 'New York', 'country': 'USA'}

######################################################################################
# 4. Sets: unordered collections of unique elements; useful for performing set operations like:
######################################################################################
# union, intersection, and difference; created using {} or set()
# Creating a set
my_set = {1, 2, 3, 4, 5}
# Adding elements to the set
my_set.add(6)
print(my_set)           # {1, 2, 3, 4, 5, 6}
# Removing elements from a set
my_set.remove(6)
print(my_set)           # {1, 2, 3, 4, 5}

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# Union
union_set = set_a.union(set_b)
print(union_set)                # {1, 2, 3, 4, 5}
# Intersection
intersection_set = set_a.intersection(set_b)
print(intersection_set)         # {3}
# Difference
difference_set = set_a.difference(set_b)
print(difference_set)           # {1, 2}
# Symmetric Difference (elements present in either set, but not both)
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Unique Elements: ", set_a ^ set_b)    # Output: {1, 2, 4, 5} SYMMETRIC DIFFERENCE
print(symmetric_difference_set)              # Output: {1, 2, 4, 5}
# Operations Tricks NOTE: ORDER MATTERS
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Subracting Sets: ", set_a - set_b)    # Output: {1, 2, 3}
print("Subracting Sets: ", set_b - set_a)    # Output: {8, 6, 7}
print("Subracting Sets: ", set_a & set_b)    # Output: {4, 5}
print("Subracting Sets: ", set_a ^ set_b)    # Output: {1, 2, 3, 6, 7, 8} SYMMETRIC DIFFERENCE


######################################################################################
# 5. Deque (Double-ended Queue): optimized list for inserting and removing items from both ends
######################################################################################
from collections import deque
# Creating a deque
my_deque = deque([1, 2, 3]) 
# Adding elements
my_deque.append(4)      # Add 4 to the right end
my_deque.appendleft(0)  # Add 0 to the left end

print(my_deque)         # deque([0, 1, 2, 3, 4])

# Removing elements
my_deque.pop()          # Remove from the right end
my_deque.popleft()      # Remove from the left end

print(my_deque)         # deque([1, 2, 3])

######################################################################################
#  6. Named Tuples: tuples with named fields  
######################################################################################
from collections import namedtuple

# Defining a named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Creating instances of the named tuple
person1 = Person(name='Alice', age=30, city='New York')
person2 = Person(name='Bob', age=25, city='San Francisco')

# Accessing elements by name
print(person1.name)    # Output: 'Alice'
print(person2.age)     # Output: 25

# Accessing elements by index (similar to regular tuples)
print(person1[2])      # Output: 'New York'

# Named tuples are immutable, so you cannot modify their values
# person1.name = 'Charlie'  # This will raise an AttributeError

# Named tuples also have some useful methods
print(person1._asdict())  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person2._fields)    # Output: ('name', 'age', 'city')

######################################################################################
# 7. Counter: counting the occurrences of elements in a collection; similar to 'defaultdict(int)'
######################################################################################
from collections import Counter

# Using Counter to count occurrences of elements in a list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(my_list)

print(counter)    # Output: Counter({4: 4, 3: 3, 2: 2, 1: 1})

######################################################################################
# 8. Stacks: LIFO data structure; elements added and removed from same end, lists can be used to implement stacks
######################################################################################
# Using a list as a stack
stack = []

# Pushing elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)        # Output: [1, 2, 3]

# Popping elements from the stack
popped_element = stack.pop()
print(popped_element)     # Output: 3
print(stack)             # Output: [1, 2]

######################################################################################
# 9. Queues: FIFO data structure; elements added to right and removed from left; implemented using lists, collections, deque, or queue module  
######################################################################################
from collections import deque

# Creating a queue using deque
queue = deque()

# Enqueue (Adding elements to the rear)
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)              # Output: deque([1, 2, 3])

# Dequeue (Removing elements from the front)
dequeued_element = queue.popleft()
print(dequeued_element)   # Output: 1
print(queue)              # Output: deque([2, 3])

######################################################################################
# 10. Heaps: specialized tree-based structure that satisfies the heap property; used for priority queues
######################################################################################
import heapq

# Creating a heap
heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Converting a list into a heap (heapify)
heapq.heapify(heap)

print(heap)        # Output: [1, 1, 2, 3, 3, 9, 4, 6, 5, 5, 5]

# Inserting elements into the heap
heapq.heappush(heap, 7)

print(heap)        # Output: [1, 1, 2, 3, 3, 9, 4, 6, 5, 5, 5, 7]

# Popping the smallest element from the heap
min_element = heapq.heappop(heap)
print(min_element)    # Output: 1
print(heap)           # Output: [1, 3, 2, 5, 3, 9, 4, 6, 5, 5, 7]

######################################################################################
# 11. Defaultdict: has a default factory function for missing keys = automatically creates missing keys with a default value when accessed
######################################################################################
from collections import defaultdict

# Using defaultdict to count occurrences of elements in a list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = defaultdict(int)

for num in my_list:
    counter[num] += 1

print(counter)    # Output: defaultdict(<class 'int'>, {1: 1, 2: 2, 3: 3, 4: 4})

######################################################################################
# 12. OrderedDict: maints the order of the keys based on the insertion order; in reg dicts, order is not guaranteed
######################################################################################
from collections import OrderedDict

# Creating an ordered dictionary
my_ordered_dict = OrderedDict()

my_ordered_dict['apple'] = 3
my_ordered_dict['banana'] = 1
my_ordered_dict['orange'] = 2

print(my_ordered_dict)    # Output: OrderedDict([('apple', 3), ('banana', 1), ('orange', 2)])

######################################################################################
# 13. ChainMap: allwos you to combine multiple dicts into a single view; maintains a list of dicts and searches through them in the order they are provided to find a key
######################################################################################
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

combined_dict = ChainMap(dict1, dict2)

print(combined_dict['a'])    # Output: 1
print(combined_dict['c'])    # Output: 3

######################################################################################
# 14. Defaultdict with List: useful for creating a dict of lists, where each key maps to a list, and new keys are automatically initialized with empty lists
######################################################################################
from collections import defaultdict

my_dict = defaultdict(list)

my_dict['fruits'].append('apple')
my_dict['fruits'].append('banana')

print(my_dict['fruits'])    # Output: ['apple', 'banana']
print(my_dict['vegetables'])    # Output: [] (automatically initialized as an empty list)

######################################################################################
# 15. Linked Lists: collection of nodes where each node points to the next noide in the sequence
######################################################################################

######################################################################################
# 16. Trees: hierarchical data structure with nodes connected by edges, commonly used for search and hierarchical representation 
######################################################################################

######################################################################################
# 17. Graphs: represent a set of vertices connected by edges, used for modeling relationships between objects 
######################################################################################

######################################################################################
# 18. Hash Tables: maps keys to values, offering fast access and search time 
######################################################################################

######################################################################################
# 19. Binary Search: search algorithm that finds the position of a target value within a sorted array 
######################################################################################

######################################################################################
# 20. Breadth-First Search: traverses a graph level by level, starting from the root node 
######################################################################################