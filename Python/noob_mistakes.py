'''
Noob Mistakes beginners make in Python
'''

# 1. Tuples #########################################################################
# Normally see tuples as such:
coordinates = (1, 2)
# Parantheses don't define a tuple, the comma does:
coordinates = () # empty tuple is exception
coordinates = (1) # partentheses used as order of ops
print(type(coordinates)) # Output: int
coordinates = 1,2
print(type(coordinates)) # Output: tuple

# Mixing up == and "is" ##############################################################
# Never use "is" for comparing values, just use ==
x: int = 100
y: int = 100
print(x == y) # Output: True
print(x is y) # Output: True

      
x: int = 100
y: int = 90
print(x == y) # Output: False
print(x is y) # Output: False

x: float = 100
y: float = 1000 / 10 
print(x, y)   # Output: 100 100.0
print(x == y) # Output: True
print(x is y) # Output: False
print(id(x))  # Output: memory address #
print(id(y))  # Output: different memory address #
print(x is y) # Output: False because different objects in memory, not values, sometimes TRUE

# Not using if __name__ = '__main__' #################################################
# for testing so you can run a module for testing
def func() -> None:
  print("My module")

# Checks if script running is current script (aka '__main__' script)
# def main() -> None:           # avoids cluttering namespace
#   func()
# if __name__ == '__main__':
#   func()


# Mixing up class attributes and instance attributes ##################################
class Car:
  # Class attributes (outside of initializer)
  # all future instances of a Car class will have this attribute
  fuel_type: str = 'electric'
  def __init__(self, brand:str) -> None:
    # instance attributes use "self"
    # "instance" is unique occurence of a class
    self.brand = brand

bmw: Car = Car('BMW')
print(bmw.fuel_type)
print(bmw.brand)
bmw.fuel_type = 'diesel' # creates new instance attribute, not class attribute
print(bmw.fuel_type)
mercedes: Car = Car('Mercedes')
print(mercedes.fuel_type)
Car.fuel_type = 'Steam powered'
volvo: Car = Car("Volvo")
print(volvo.fuel_type)
print(mercedes.fuel_type)
print(bmw.fuel_type)