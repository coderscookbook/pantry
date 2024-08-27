"""
SYNTAX
  [start:stop:step]
  - start is inclusive
  - stop is exclusive
  - step can be negative or positive
"""

text: str = '1234567890'
print("1: ", text[5:10])        # Output: 567890
print("2: ", text[:10])         # Output: 1234567890
print("3: ", text[1:8:2])       # Output: 2468
print("4: ", text[0:9:3])       # Output: 147
print("5: ", text[-1:-8:-2])    # Output: 0864
print("6: ", text[1:-10:-1])    # Output: 2
print("7: ", text[-1:-10:-1])   # Output: 098765432
print("8: ", text[2:7])         # Output: 34567
print("9: ", text[:4])          # Output: 1234
print("10: ", text[3:9:2])      # Output: 468
print("11: ", text[::3])        # Output: 1470
print("12: ", text[7:2:-2])     # Output: 864 
print("13: ", text[5::-1])      # Output: 654321
print("14: ", text[-3:])        # Output: 890
print("15: ", text[8:3:-1])     # Output: 98765
print("16: ", text[9:3:-1])     # Output: 098765
print("17: ", text[-2:-6:-1])   # Output: 9876
print("18: ", text[9:3:-2])     # Output: 086
print("19: ", text[9:3:2])      # Output: 
print("20: ", text[9:3:])       # Output: 

# Reusing slicing - use the built-in slice function
my_slice: slice = slice(5, 10)
my_slice: slice = slice(None, 10)      # replaces [:10]
print(text[my_slice])           # Output: 1234567890