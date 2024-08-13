from keyword import kwlist, softkwlist

def display_keywords() -> None: 
  print('Keywords:')
  for i, kw in enumerate(kwlist, start=1):
    print(f'{i:2}: {kw}')

  print('Soft keywords:')
  for i, skw in enumerate(softkwlist, start=1):
    print(f'{i:2}: {skw}')
  
def main() -> None: 
  display_keywords()
  
if __name__ == '__main__':
  # main()

# and
  if (1+1) and (True + True):
    print('TRUE')

# OUTPUT w/ added examples:
# Keywords:
#  1: False - constant for 0 
has_money: bool = False
print(has_money)  # Output: False
print(int(False)) # Output: 0

#  2: None - absence of value
from typing import Any
data: Any = None
print(data) # Output: None

class User: 
  ...
selected_user: User | None = None
print(selected_user)  # Output: None 

#  3: True - constant for 1 
has_money: bool = True
print(has_money)    # Output: False
print(int(True))    # Output: 0
print(True + True)  # Output: 2

#  4: and - two or more conditions return True
name: str = 'Bob'
age: int = 19
if len(name) > 0 and age > 18:
  print('User is eligible to sign up.')

#  5: as - to give an alias to a module
import math as m 
from random import randint as ri
m.cos(10) 
ri(10,20) # ranges are inclusive

with open('text.txt', 'r') as file:
   print(file)

#  6: assert - makes sure somethign specific is there before moving on
db: str | None = 'users.db' # if = None, raises assert error
assert db, 'Cannot run program w/out the database'

limit: int = 10
n: int = 2
assert n < limit, f'{n} is not less than the limit ({limit})'

#  7: async - SEE ASYNC.py module
import asyncio # must be imported
async def main () -> None:
  print('I am an async function!')

# if __name__ == '__main__':    # Uncomment to run
  # asyncio.run(main=main())

#  8: await - waits for function to finish before moving on
from asyncio import Future
async def my_task(no: int) -> dict:
  print('Starting task...') 
  await asyncio.sleep(2)
  return {'task': no}

async def main() -> None:
  tasks: Future = asyncio.gather(my_task(1),
                                 my_task(2),
                                 my_task(3))
  results: list[dict] = await tasks 
  print(results)

# if __name__ == '__main__':    # Uncomment to run
  # asyncio.run(main=main())


#  9: break - exits a loop prematurely
for i in range(10):
  if i == 5:
    break
  else:
    print(i)
print('Done!')

# 10: class - creating a class
class Person:
  def __init__(self, name: str) -> None:
    self.name = name
  
  def work(self) -> None:
    print(f'{self.name} is working...')

# 11: continue - skip code and continue to next item in iteration 
names: list[str] = ['Tom', 'Bob', 'James']
for name in names:
  if name == 'Bob':
    print('We do not say hello to Bob')
    continue
  print(f'Say hello to {name}')

# 12: def - definition or define
def func() -> None:
  print('This function is defined')
  
# 13: del - delete an object
name: int = 10
print(name)
del name
print(name)

# 14: elif - "else if" in conditional statements, middle layer in else-if statements
weather: str = 'rainy'
if weather == 'rainy':
  print('Bring an umbrella')
elif weather == 'sunny':
  print('Bring sunblock')
elif weather == 'overcast':
  print('Bring a coat')

# 15: else - conditional statements clause, if no conditions are met
weather: str = 'rainy'
if weather == 'rainy':
  print('Bring an umbrella')
elif weather == 'sunny':
  print('Bring sunblock')
elif weather == 'overcast':
  print('Bring a coat')
else:
  print('Weather is unknown')

# 16: except - catch exceptions
from typing import Never
def dangerous_code() -> Never:
  raise ValueError('Bad Value')
try:
  dangerous_code()
except ValueError as e:
  print(f'Yo, you messed up: {e}')

# 17: finally - runs no matter what happens in the try-except block
from typing import Never
def dangerous_code() -> Never:
  raise ValueError('Bad Value')
try:
  dangerous_code()
except ValueError as e:
  print(f'Yo, you messed up: {e}')
finally:
  print('Finally: I run no matter what happens')

# 18: for - loops through an iteratable
from typing import Any
elements: list[Any] = [1, 'text', True, 'Bob']
for element in elements:
  print(element)

# 19: from - importing specific functionality from a module
from typing import Any

# 20: global - refer to objects in a global namespace
name: str = 'Bob'
def change_name() -> None:
  global name
  name = 'James'  # 'name' refers to local scope
change_name()
print(name)

# 21: if - conditional statement
age: int = 38
if int > 20:
  print('You are old')

# 22: import - imports modules at the top of a script
import json

# 23: in - if a certain element is IN an iterable/perform membership checks
names: list[str] = ['Bob', 'Jill', 'Jason']
for name in names:
  print(name)

if 'Bob' in names:
  print('We found Bob')
  

# 24: is - does not compare value, compares memory address
class Fruit:
  ...
apple: Fruit = Fruit()
other_apple = apple
print(apple is other_apple) # point to exact same memory address

# 25: lambda -  nameless function, functions used once
from typing import Callable, Any
p = lambda x: print(x)
p(10)

(lambda x: print(x))(10)

def print_results(func: Callable, elements: list[Any]):
  for elem in elements: 
    print(func(elem))
print_results(lambda x: x*2, elements=[1, 2, 3])

# 26: nonlocal - refer to object in an outer scope
def func() -> None:
  item: str = 'candle'
  def inner_func() -> None:
    nonlocal item
    print(item)
  inner_func()
func()

# 27: not - python does not like != comparison operator, use this instead
names: list[str] = ['Bob', 'Jill', 'Jason']
if 'Bob' not in names:
  print('Bob is lost...')

selected_user: str | None = None
if selected_user is not None:
  print(f'You have selected: {selected_user}')
else:
  print('No user selected...')

# 28: or - true if one or more statements are True 
a, b, c = 5, 10, 20
if c > a or a == b:
  print('One of the conditions was satisfied')

# 29: pass - instead of doing nothing
def func() -> None:
  pass

class Fruit:
  pass

# 30: raise - manually raise an exception
raise Exception('Manually raised an exception on this line')

# 31: return - returning a value from a function
from datetime import datetime
def get_time() -> str: 
  now: datetime = datetime.now()
  return now
print(get_time())

# 32: try - clause that runs code that might raise an exception first, requires an except clause after it
try: 
  result: float = 1_000_000 / 0
except ZeroDivisionError: 
  print("Cannot divide by zero")

# 33: while - loop that runs while a condition is true
import time
is_connected: bool = True
i: int = 1
while is_connected:
  if i == 3:
    is_connected = False
  print(f'Connected for: {i}s')
  time.sleep(1)
  i += 1
print('Connection lost...')

# 34: with - closes a function block automatically
with open('text.tx.', 'r') as file:
  text: str = file.read()
  print(text)

# 35: yield - once you yield a value, it disappears from that generator
from typing import Generator
def generate_numbers(limit: int) -> Generator:
  for i in range(0, limit):
    yield i
numbers: Generator = generate_numbers(limit=10)
print(next(numbers))  # Output: 0
print(next(numbers))  # Output: 1
print(list(numbers))  # Output: [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Soft keywords:
#  1: _ - NOTE: see underscore_character.py 

#  2: case - used in match-case statements
weather: str = 'rainy'
match weather:
  case 'rainy':
    print('Bring an umbrella')
  case 'sunny':
    print('Bring sunblock')
  case 'overcast':
    print('Bring a coat')
  case _:
    print('Weather unknown')

#  3: match - used in match-case statements
weather: tuple[str, int] = 'rainy', 6
match weather:
  case 'rainy', severity if severity <=5:
    print(f'Rain({severity})')
  case 'rainy', severity if severity > 5:
    print(f'Very Hard Rain! ({severity})')
  case 'overcast', severity:
    print(f'Clouds visible. ({severity})')
  case _:
    print('Weather unknown')

#  4: type - define custom types as of python 3.12
type IntOrStr = int | str
var: IntOrStr = 0
var: IntOrStr = 'happy'
var: IntOrStr = [1, 2, 3] # gives a warning with new static checker