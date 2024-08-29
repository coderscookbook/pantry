#######################################################################################
# "*" (unpacking operator): unpacks elements of a list 
#######################################################################################
numbers = [1, 2, 3]
print(*numbers)   # Output: 1 2 3


#######################################################################################
# all(): returns 'True' if all elements of a list are 'True' or list is empty 
#######################################################################################
numbers = [1, 2, 3, 4, 5]
result = all([x > 0 for x in numbers])
print(result)     # Output: True


#######################################################################################
# any(): returns 'True' if at least one element of a list is 'True'
#######################################################################################
numbers = [0, 0, 0, 4, 0, 'String']
result = any(isinstance(element, str) for element in numbers)
print(result)  # Output: True


#######################################################################################
# append(): adds elements to the end of the list
#######################################################################################
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)     # Output: ['apple', 'banana', 'cherry', 'orange']


#######################################################################################
# clear(): removes all elements from the list
#######################################################################################
cars = ["Lexus", "Toyota", "Mercedez"]
cars.clear()
print(cars)       # Output: []


#######################################################################################
# copy(): creates shallow copy of the list, does not affect original array
#######################################################################################
fruits = ["apple", "banana", "cherry"]
fruits_copy = fruits.copy()
print(fruits_copy)      # Output: ['apple', 'banana', 'cherry']


#######################################################################################
# count(): returns number of elements with the specified value
#######################################################################################
fruits = ['apple', 'banana', 'cherry', 'banana']
count = fruits.count('banana')
print(count)      # Output: 2

#######################################################################################
# deepcopy(): used when copying nested lists, ensures new changes dont affect og list
#######################################################################################
import copy
nested_list = [[1, 2], [3, 4]]
copied_list = copy.deepcopy(nested_list)
copied_list[0][0] = 99
print(nested_list)    # Output: [[1, 2], [3, 4]]
print(copied_list)    # Output: [[99, 2], [3, 4]]


#######################################################################################
# del(): deletes elements from the list using the index or slice
#######################################################################################
numbers = [1, 2, 3, 4, 5]
del numbers[1]
print(numbers)  # Output: [1, 3, 4, 5]


#######################################################################################
# enumerate(): returns an enumerate object that contains pairs of index and value
#######################################################################################
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)
# Output:
# 0 apple
# 1 banana
# 2 cherry


#######################################################################################
# extend(): add the elements of an iterable to the end of a current list
#######################################################################################
fruits = ["apple", "banana", "cherry"]
additional_fruits = ["orange", "grape"]
fruits.extend(additional_fruits)
print(fruits)     # Output: ['apple', 'banana', 'cherry', 'orange', 'grape']

#######################################################################################
# filter(): 
#######################################################################################
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

#######################################################################################
# index(): returns index of first element with specified value
#######################################################################################
fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')
print(index)      # Output: 1


#######################################################################################
# insert(): adds element at the specified position to a list
#######################################################################################
# syntax: arr.insert(position, element)
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3,4)
print(numbers)    # Output: [1, 2, 3, 4, 5, 6, 7]


#######################################################################################
# join(): joins all elements ina list into a string
#######################################################################################
words = ["Hello", "world"]
sentence = " ".join(words)
print(sentence)   # Output: "Hello world"


#######################################################################################
# list(): converts an iterable into a list
#######################################################################################
string = "hello"
string_list = list(string)
print(string_list)   # Output: ['h', 'e', 'l', 'l', 'o']

iterable = range(3)
numbers = list(iterable)
print(numbers)       # Output: [0, 1, 2]


#######################################################################################
# len(): gets the length of the array
#######################################################################################
numbers = [1, 2, 3, 4, 5, 6]
length = numbers.len()
print(length)     # Output: 6


#######################################################################################
# map(): applies a function to all elements in a list
#######################################################################################
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


#######################################################################################
# max(): returns the max value in the list
#######################################################################################
numbers = [4, 2, 1, 3]
maximum = max(numbers)
print(maximum)   # Output: 4

#######################################################################################
# min(): returns the min value in the list
#######################################################################################
numbers = [4, 2, 1, 3]
minimum = min(numbers)
print(minimum)   # Output: 1

#######################################################################################
# pop(): removes element at the specified position in a list
#######################################################################################
numbers = [1, 2, 3, 4, 4, 5, 6, 7]
numbers.pop(3)
print(numbers)    # Output: [1, 2, 3, 4, 5, 6, 7]

#######################################################################################
# remove(): removes first item in the list with the specified value 
#######################################################################################
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)     # Output: ["apple", "cherry", "banana"]


#######################################################################################
# reverse(): reverses the order of the list
#######################################################################################
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)     # Output: ['cherry', 'banana', 'apple']

#######################################################################################
# reversed(): returns an iterator that accesses the given list in reverse order
#######################################################################################
numbers = [1, 2, 3, 4]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)  # Output: [4, 3, 2, 1]


#######################################################################################
# slice(): returns a slice object that can be used to slice a list
#######################################################################################
numbers = [1, 2, 3, 4, 5]
sliced_numbers = numbers[slice(1, 4)]
print(sliced_numbers)  # Output: [2, 3, 4]


#######################################################################################
# sort(): sorts the list in ascending order
#######################################################################################
# syntax: arr.sort(*, key=value, reverse=bool)
numbers = [4, 2, 1, 3]
numbers.sort()
print(numbers)    # Output: [1, 2, 3, 4]
numbers.sort(reverse=True)
print(numbers)    # Output: [4, 3, 2, 1]
numbers.sort(key=lambda x: x >= 3)
print(numbers)    # Output: [2, 1, 4, 3]


#######################################################################################
# sorted(): returns new sorted list without changing the original list 
#######################################################################################
numbers = [4, 2, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4]
print(numbers)         # Output: [4, 2, 1, 3]


#######################################################################################
# sum(): returns the sum of all elements in the list
#######################################################################################
numbers = [4, 2, 1, 3]
total = sum(numbers)
print(total)    # Output: 10


#######################################################################################
# zip(): combines elements from two or more lists into tuples
#######################################################################################
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = list(zip(list1, list2))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


#######################################################################################
# Itertools: module functions that operate on lists
# - itertools.chain: Combines multiple iterables into a single one.
# - itertools.islice: Allows slicing of iterables.
# - itertools.permutations and itertools.combinations: Generate permutations or combinations of elements in the list.
#######################################################################################
import itertools
combined = list(itertools.chain([1, 2], [3, 4]))
print(combined)  # Output: [1, 2, 3, 4]


#######################################################################################
# Bisect: module module used to maintain a list in sorted order
# - bisect.bisect(list, element): Finds the position to insert the element to keep the list sorted.
# - bisect.insort(list, element): Inserts an element in the list while maintaining order
#######################################################################################
import bisect
numbers = [1, 2, 4, 5]
bisect.insort(numbers, 3)
print(numbers)  # Output: [1, 2, 3, 4, 5]
