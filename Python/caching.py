'''
CACHING
- technique used to store the results of expensive function calls and reuse the cached result when the same inputs occur again
- aka: storing frequently accessed data in memory to improve performance
- improves performance, especially in cases where the function is called multiple times with the same arguments
- Key Points:
  - Purpose: speed up the execution of functions by avoiding repeated computations for the same input
  - Common Usage: useful in situations like recursive algorithms, web requests, and database queries where recalculating the result is costly
  - Libraries: the 'functools' module in Python provides a built-in way to cache function results
- Strategies:
  - Write-through: update both cache and underlying storage simultaneously
  - Write-behind: update the cache first and asynchronously update the underlying storage later
  - Read-through: if cache miss occurs, fetch the data from the underlying storage system and store it in cache
- Cache Invalidation:
  - Time-based: invalidate cache entries after a certain amount of time
  - Size-based: invalidate cache entries when the cache reaches a certain size
  - Manual: manually invalidate cache entries based on specific events or conditions
'''

#######################################################################################
# EXAMPLES                                                                            #
#######################################################################################
# EXAMPLE: In-memory Caching
from os import removedirs
import time
cache = {}
def expensive_function(x):
  if x in cache: 
    return cache[x]
  result = x * x    # perform expensive computation
  cache[x] = result
  return result

# testing
start_time = time.time()
result = expensive_function(10)
end_time = time.time()
print("Time taken:", end_time - start_time)


# EXAMPLE: Database-level Caching
import sqlite3
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# create a table for caching results
c.execute('''CREATE TABLE IF NOT EXISTS cache (
                key TEXT PRIMARY KEY,
                value TEXT
            )''')

def expensive_function(x):
  c.execute("SELECT value FROM cache WHERE key=?", (x,))
  result = c.fetchone()
  if result:
    return result[0]
  # perform expensive computation
  c.execute("INSERT INTO cache VALUES (?, ?)", (x, result))
  conn.commit()
  return result


# EXAMPLE: Third-party Caching Libraries
import redis 
r = redis.Redis()

def expensive_function(x):
  result = r.get(str(x))
  if result: 
    return result.decode()
  # perform expensive computation
  r.set(str(x), result)
  return result
import functools                                                                      


# EXAMPLE: Using functools
@functools.lru_cache(maxsize=128)
def fibonacci(n):
  if n < 2:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)
  
# testing the cache
print(fibonacci(10))  # Output: 55
print(fibonacci.cache_info())  # Output: CacheInfo(hits=8, maxsize=128, currsize=11)
'''
EX.1 EXPLANATION
- @functools.lru_cache(maxsize=128): decorator to enable caching for function
  - maxsize = # of most recent function calls to cache 
  - LRU (Least Recently Used): algorithm used to discard the least recently used items when the cache is full
- Potential Drawbacks:
  - cached results consume memory, important to set appropriate 'maxsize'
  - cache staleness: if underlying data changes, the cache might return outdated results unless manually invalidated
'''

# EXAMPLE 2: Custom Caching Example
def custom_cache(func):
  cache = {}

  def wrapper(*args):
    if args in cache:
      return cache[args]
    result = func(*args)
    cache[args] = result
    return result

  return wrapper

@custom_cache
def expensive_function(x):
  # simulating a costly operation
  return x * x

# testing
print(expensive_function(10))   # Output: 100
print(expensive_function(10))   # Output: 100 (cached)
'''
EX.2 EXPLANATION
- Custom Decorator: function stores results in a dictionary
- Wrapper Function: checks if the results for the given args exists in the cache, if not, compute and store
- Flexibility: allows custom logic, such as cache eviction or conditional caching
'''