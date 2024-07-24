''' 
key is to use a stack data structure
- if "(", append to stack
- if ")", pop "(" from stack
- must end up with empty stack
- Two Cases that fail:
  1. ())hi
  2. (((hi))
'''

def BracketMatcher(string):
  stack = []
  
  for letter in string :
    if letter == '(':
      stack.append(letter)
    elif letter == ')':
      if len(stack) == 0:
        return 0
      else:
        stack.pop()
        
  return 1 if len(stack) == 0 else 0

# Example usage
print(BracketMatcher("()"))   # Output: 1
print(BracketMatcher("(())")) # Output: 1
print(BracketMatcher("(()"))  # Output: 0
print(BracketMatcher(")("))   # Output: 0