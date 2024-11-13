# TryExcept Scope for variable changes
e = 'l'
try: 
  print(f'Converting {e} to int...')
  print(int(e))
except ValueError as e:
  print('ERROR:', e)
  # Prints a value error

print(e)  # Prints "NOT DEFINED" error, TryExcept block deletes e from scope

''' 
---FULL OUTPUT---
Converting l to int...
ERROR: invalid literal for int() with base 10: 'l'
Traceback (most recent call last):
  File "/Users/soigne/PROJECTS/PANTRY/Python/_Quirks.py", line 10, in <module>
    print(e)  # Prints "NOT DEFINED" error, TryExcept block deletes e from scope
          ^
NameError: name 'e' is not defined
'''