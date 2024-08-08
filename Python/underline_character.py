# Ways to Use Underline(_) in Python

# 1. Big numbers in python
big_number: int = 1_000_000_000_000
print(big_number) # Output: 1000000000000

# 2. Use for unimportant values
# - scenario: we want to extract values from a tuple but don't consider all the values to be important
stats: tuple[str, str, int] = ['Bob', 'Pilot', 27]
name, _, age = stats
print(f'{name}')
print(f'{age}')
print(_) # still holds value but not important to progammer

# 3. Star underscore
values: list[int] = [1, 2, 3, 4, 5]
first, *_, last = values
print(first, last, sep=', ')  # output: 1,5
print(_)                      # output: [2, 3, 4]

# 4. For loops
# - scenario: some cases don't care about iterator name
for _ in range(3):
  print('For loop')

[print('yo') for _ in range(3)] # list comprehension

# 5. Semi-private variables
# used only internally in class or subclass (naming convention only)
from uuid import uuid4, UUID

class Lamp:
  def __init__(self, brand: str) -> None:
    self.brand = brand
    self._id: UUID = uuid4()
    
  def get_id(self) -> UUID:
    return self._id
    
# 6. Name Mangling
# - mangles name at runtime, helps with name collisions
class Lamp:
  def __init__(self, brand: str) -> None:
    self.brand = brand
    self.__hidden_id: UUID = uuid4()
    
pam: Lamp = Lamp(brand='Pam')
print(pam.brand)
# print(pam.__hidden_id)    # doesn't work 
print(pam._Lamp__hidden_id) # works (hint from console error message)

# 7. Dunder methods
from typing import Self 

class CustomNumber:
  def __init__(self, value: int) -> None:
    self.value = value
  
  # def __add__(self, other: Self) -> int:
  #   return(self.value + other.value) * 1_000_000_000
  
  # def __repr__(self) -> str:
  #   return f'CustomNumber(value={self.value})'

   # allows use of pipeline( | )
  def __or__(self, other: Self) -> str:
    return f'{self.value} | {other.value}'
  

n1: CustomNumber = CustomNumber(10)
n2: CustomNumber = CustomNumber(300)
print(n1)
print(n1 + n2)
print(n1 | n2)

# 8. Using reserved names (want to use, but can't without _)
class = 'bob'
_class = 'bob'
for = 'jack'
for_ = 'jack'

# 9. Default cases
gangsta_weather: str = 'rain'
match gangsta_weather: 
  case 'rain':
      print('Yo, find yourself an umbrella')
  case 'sunny':
      print('Yo, find yourself sunblock')
  case _:
      print('Yo, I have no idea what the weather means')
