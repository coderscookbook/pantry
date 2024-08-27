import typing as t
import collections.abc as c

def say_hello(names: t.Iterable) -> None:
  for name in names:
    print(name)

# because argument passed is of type 'Iterable', function works 
say_hello(['Bob', 'Luigi'])   # Output: Bob Luigi
# won't work
say_hello(123) # Output: error, not type 'Iterable'

#### BUT IT"S DEPRECATED since Python 3.9!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#### AND THERE ARE NO DEPRECATION WARNINGS FOR TYPING MODULE!!!!!!!!!!!!!!!!!!!!!!!

###### INSTEAD USE COLLECTIONS.ABC
def say_hello2(names: c.Iterable) -> None: 
  for name in names:
    print(name)
    
    
#### USE A CALLABLE (also look up PARTIALS)
def repeat(func: t.Callable, times: int) -> None:
  for i in range(times):
    func()

def hello() -> None:
  print("Hello")

repeat(hello, times=3)

# callable/partials/currying
from collections.abc import Callable

def multiply_setup(a: float) -> Callable:
  def multiply(b: float) -> float:
    return a * b
  
  return multiply

double: Callable = multiply_setup(2)
triple: Callable = multiply_setup(3)

print(double(5))
print(double(3))
print(double(100))
