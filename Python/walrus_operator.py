'''
Python 3.8+
  - allows you to assign a value to a variable as part of an expression
  - esp. useful when you want to BOTH evaluate and use a value within a single line of code
    -- often within conditions, loops, and comprehensions
  - makes code more conscise and readable
'''

# EXAMPLE 1: Within a While Loop
# WITHOUT:
data = input("Enter data: ")
while data: 
  print(f"You entered: {data}")
  data = input("Enter data: ")
#WITH:
while (data := input("Enter data: ")):
  print(f"You entered: {data}")


# EXAMPLE 2: Within List Comprehensions
# WITHOUT:
lines = input("Enter lines: ")
results = []
for line in lines:
  stripped = line.strip()
  if stripped:
    results.append(stripped)
# WITH: W.O. allows to strip the line and check if it's non-empty
results = [stripped for line in lines if (stripped := line.strip())]


# EXAMPLE 3: Within List Comprehensions
# WITHOUT:
n = len(data)
if n > 10:
  print(f"Data is too long ({n} elements)")
# WITH:
if (n := len(data)) > 10:
  print(f"Data is too long ({n} elements)")


# EXAMPLE 4: Combining filtering and transformation
def transform(value):
  return value * 2

values    = [1, 20]
threshold = 5
filtered_transformed = []

# WITHOUT: 
for value in values:
  transformed = transform(value)
  if transformed > threshold:
    filtered_transformed.append(transformed)
# WITH:
filtered_transformed = [transformed for value in values if (transformed := transform(value)) > threshold]
print(filtered_transformed) # [40] for both
