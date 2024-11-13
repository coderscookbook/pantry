from functools import lru_cache
import time

'''
Example 1: Recursive function calculation
- @lru_cache: saves result of each call to the function so it doesn't need to run calc every time
'''
@lru_cache
def fib(n: int) -> int:
  if n<=1:
    return n
  else:
    return fib(n-1) + fib(n - 2)

start = time.time()
for i in range(0,100):
  print(f'{i}: {fib(i)}')
end = time.time()
print("@LRU_CACHE TIME: ", end - start)
  

'''
Example 2: Implement Cache programmatically (behind the scenes look at cache)
- recursive Fibonacci function using dict as cache
- NOTE may be faster than using lru_cache
'''
# dict to store previously computed Fibonacci values
fibonacci_cache = {}

def fibonacci(n):
  # Check if the value is in the cache
  if n in fibonacci_cache:
    return fibonacci_cache[n]
  
  # base cases
  if n <=1:
    return n
  
  # recursive calculation
  result = fibonacci(n-1) + fibonacci(n-2)
  
  # store the result in the cache
  fibonacci_cache[n] = result
  return result

# Usage
start = time.time()
# print(fibonacci(40))
for i in range(0,100):
  print(f'{i}: {fibonacci(i)}')
end = time.time()
print("PROGRAMATICALLY: ", end - start)
  

'''
Example 3: Using cache size limit (LRU-like)
- using collections.OrderedDict to implement limited-size cache
- removes oldest items when cache reaches a specific size
'''
from collections import OrderedDict

class LimitedSizeCache:
  def __init__(self, max_size=128):
    self.cache = OrderedDict()
    self.max_size = max_size
    
  def get(self, key):
    if key in self.cache:
      # move the accessed item to the end (most recent)
      self.cache.move_to_end(key)
      return self.cache[key]
    return None

  def set(self, key, value):
    self.cache[key] = value
    # move the item to the end (most recent)
    self.cache.move_to_end(key)
    # if the cache exceeds the max size, remove the oldest item
    if len(self.cache) > self.max_size:
      self.cache.popitem(last=False)

# create a LimitedSizeCache instance for Fibonacci
fibonacci_cache = LimitedSizeCache(max_size=128)

def fibonacci_LSC(n):
  # check if result is cached
  cached_result = fibonacci_cache.get(n)
  if cached_result is not None:
    return cached_result
  
  # base case
  if n <= 1:
    return n
  
  # calculate and cache the result
  result = fibonacci_LSC(n-1) + fibonacci_LSC(n-2)
  fibonacci_cache.set(n, result)
  return result

# Usage
start = time.time()
# print(fibonacci_LSC(40))
for i in range(0,100):
  print(f'{i}: {fibonacci_LSC(i)}')
end = time.time()
print("PROGRAMATICALLY_LSC: ", end - start)
