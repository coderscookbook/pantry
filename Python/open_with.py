path = 'directory/file_name'

# Need to close file object manually
f = open(path)
print(type(f))  # <class '_io.TextIOWrapper'>
f.close()

# Automatic file closure using 'with'-block
with open(path) as f:
  print(type(f))  #<class '_io.TextIOWrapper'>


##############################################################################
# MODES: r
##############################################################################

# 'r' = read is the default mode
with open(path, 'r') as f:
  print(type(f))

## Read entire file into a single string: read()
with open(path) as f:
  s = f.read()
  print(type(s))
  # <class 'str'>
  print(s)
  # line 1
  # line 2
  # line #!/usr/bin/env python3
  
# Assigned variable remains accessible outside the with-block
with open(path) as f:
  s = f.read()

print(s)
# line 1
# line 2
# line #!/usr/bin/env python3

# Assigned variable remains accessible outside the with-block
with open(path) as f:
  s = f.read()

print(s)
# line 1
# line 2
# line #!/usr/bin/env python3

## Read entire file into a list: readlines()
with open(path) as f:
  l = f.readlines()
  print(type(l))
  # <class 'list'>
  print(l)
  # ['line 1\n', 'line 2\n', 'line 3']

## Remove newline character, use list comprehension: rstrip() on each el.
with open(path) as f:
  l_strip = [s.rstrip() for s in f.readlines()]
  print(l_strip)
  # ['line 1', 'line 2', 'line 3']
  
# Read a file line by line: readline()
# retrieve each line as a string including newline char
# repr() is used to display the newline char as is (see python/random.py)
with open(path) as f:
  for s_line in f:
    print(repr(s_line))
    # 'line 1\n'
    # 'line 2\n'
    # 'line 3\n'
## to read one line at a time use next() - error if no more lines to read
with open(path) as f:
  print(repr(next(f)))
  print(repr(next(f)))
  print(repr(next(f)))
  print(repr(next(f)))
  # 'line 1\n'
  # 'line 2\n'
  # 'line 3\n'
  # raises ERROR
# readlin() can also retrieve one line at a time but does not raise error after EOF
with open(path) as f:
  print(repr(f.readline()))
  print(repr(f.readline()))
  print(repr(f.readline()))
  print(repr(f.readline()))
  # 'line 1\n'
  # 'line 2\n'
  # 'line 3\'
  # ''


##############################################################################
# MODES: w
##############################################################################

# NOTE: Using mode='w' can accidentally overwrite an existing file!
# File to write to
path_w = 'path'
# String to write - write() only accepts string objects to be written
s = 'New file'
with open(path_w, 'w') as f:
  f.write(s)
with open(path_w) as f:
  print(f.read())

# Strings containing newline chars are written without any modification
s = 'New line 1\nNew line 2\nNew line 3'
with open(path_w, mode='w') as f:
  f.write(s)
with open(path_w) as f:
  print(f.read())
  # New line 1
  # New line 2
  # New line 3

## Write a list of strings to a file, using: writelines()
# - method does NOT automatically insert line breaks
# - writeline() only accepts list of strings
l = ['One', 'Two', 'Three']
with open(path_w, mode='w') as f:
  f.writelines(l)
with open(path_w) as f:
  print(f.read())
  # OneTwoThree
# - to write each element on a separate line, create a string containing 
# - newline chars by using the join() method
with open(path_w, mode='w') as f:
  f.write('\n'.join(l))
with open(path_w) as f:
  print(f.read())
  # One
  # Two
  # Three

## Write an empty file
with open('path_to_new_file', 'w'):
  pass


## Use the os.path.isfile() function from os.path -> check if file exists
import os
if not os.path.isfile(path_w):
  with open(path_w, mode='w') as f:
    f.write(s)

##############################################################################
# MODES: x
##############################################################################

# NOTE: to create a new file only if it does not already exist
# - if the specified file exists, a FileExistsError will be raised
try:
  with open(path_w, mode='x') as f:
    f.write(s)
except FileExistsError:
  pass


##############################################################################
# MODES: a
##############################################################################

# Append to a file







