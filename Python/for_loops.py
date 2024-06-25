'''
For loops are used for iterating over a sequence (list, tuple, dictionary, set, or string)
  - this is LESS like the FOR KEYWORD in other languages
  - works more like an iterator method as found in other OOP languages
'''

fruits = ['apple', 'orange', 'cherry']
for x in fruits:
  print(x)                  # apple orange cherry

# Looping through a string
for x in "banana":
  print(x)                  # b a n a n a
  
  
# BREAK Statement
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
  print(x)
  if x == "banana":
    break                   # apple banana

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
  if x == "banana":
    break                   
  print(x)                  # apple 


# CONTINUE Statement
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
  if x == "banana":
    continue                   
  print(x)                  # apple cherry



