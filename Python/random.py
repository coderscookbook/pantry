##############################################################################

# Default values of encoding arguments depend on the platform
# To check use:
import locale
print(locale.getpreferredencoding()) # currently prints UTF-8

##############################################################################

# repr() method in Python returns a string respresentation of an object
# intended for developers rather than end-users
# - aims to product a string that coudl be used to recreate the object
# - string is more detailed an un-ambiguous compared to str from 'str()'
# - call repr() on an object, when passed to 'eval()', would recreate object
# - useful for debugging and logging

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"Point({self.x}, {self.y})"

# Create a Point object
p = Point(3,4)
# Using repr() to get a string representation of the object
print(repr(p)) # Output: Point(3, 4)

##############################################################################




