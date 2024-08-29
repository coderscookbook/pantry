# #######################################################################################
# # 1. Basic Recursion Example: Factorial
# #######################################################################################
# def factorial(n):
#   print("n: ", n)
#   if n == 1:
#     return 1  # base case
#   else: #return n * factorial(n - 1) # recursive case
#     result = n * factorial(n - 1) 
#     print(f'{n} * factorial({n} - 1):', result)
#     return result
# # usage
# print(factorial(5)) # Output: 120
# '''
# Explanation:
#   Base Case:
#     When n is 1, the function directly returns 1. This is the stopping condition for the recursion.

#   Recursive Case:
#     For n greater than 1:
#       - The function calculates n * factorial(n - 1).
#       - This means it multiplies n by the factorial of n - 1.
#       - The factorial(n - 1) part is where the recursion happens. The function calls itself with a smaller argument (n - 1).
#       - This process continues until the base case is reached.

#   Example:
#     Let's calculate factorial(5):
#       Step 1: factorial(5) is called.
#       Step 2: Since 5 is not 1, the recursive case is executed:
#         5 * factorial(4)
#       Step 3: factorial(4) is called:
#         4 * factorial(3)
#       Step 4: factorial(3) is called:
#         3 * factorial(2)
#       Step 5: factorial(2) is called:
#         2 * factorial(1)
#       Step 6: factorial(1) is called:
#         This is the base case, so it returns 1.
#       Step 7: Working backwards:
#         2 * 1 = 2
#         3 * 2 = 6
#         4 * 6 = 24
#         5 * 24 = 120
# '''

# #######################################################################################
# # 2. Recursion with Strings: Reverse a String
# #######################################################################################
# def reverse_string(s):
#   print("String: ", s)
#   if len(s) == 0: # base case: if the string is empty, return an empty string
#     return ""
#   else: # return s[-1] + reverse_string(s[:-1])
#     char = s[-1]
#     print("Char: ", char)
#     rstr = reverse_string(s[:-1])
#     print("RevString: ", rstr)
#     return char + rstr
# print(reverse_string("hello"))  # Output: olleh


#######################################################################################
# 3. Showing the stack for recursive cases (See also file: merge_sort.py)
#######################################################################################
def merge_sort(arr, depth=0):
    indent = "  " * depth
    print(f"\n{indent}merge_sort({arr})")

    if len(arr) <= 1:
        print(f"{indent}Returning: {arr}")
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], depth + 1)  # Recursively sort the left half
    right_half = merge_sort(arr[mid:], depth + 1)  # Recursively sort the right half

    result = merge(left_half, right_half, depth + 1)
    print(f"{indent}Merged {left_half} and {right_half} into {result}")
    return result

def merge(left, right, depth):
    indent = "  " * depth
    result = []
    i = j = 0
    print(f"{indent}Merging: {left} and {right}")

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    print(f"{indent}Result: {result}")
    return result

# Example usage:
arr = [1, 2, 3, 4]
sorted_arr = merge_sort(arr)
print(f"Final sorted array: {sorted_arr}")
