''' 
lambda_expr ::= "lambda" [parameter_list] ":" expression

Lambda expressions (sometimes called lambda forms) are used to create
anonymous functions. The expression "lambda parameters: expression"
yields a function object.  The unnamed object behaves like a function
object defined with:

   def <lambda>(parameters):
       return expression

See section Function definitions for the syntax of parameter lists.
Note that functions created with lambda expressions cannot contain
statements or annotations.

TIPS:
1. keep lambdas simple
'''

# EXAMPLE 1:
# Not Required to use lambdas
from typing import Callable, Iterator # for use with type annotation
from itertools import starmap #function to be used with lambdas

def int_to_x(n: int) -> str:
    return n * 'X'

int_to_x2: Callable[[int], str] = lambda n: n * 'X' # anonymous function
# int_to_x2 = lambda n: n * 'X'


# EXAMPLE 2: where you should use lambdas
mapped: Iterator[str] = map(int_to_x, [1,2,3,4]) # becomes following line
mapped: Iterator[str] = map(lambda n: n * 'X', [1,2,3,4]) # because function only used once
print(list(mapped))


# EXAMPLE 3: 3 ways to define a function that is used only once
# example data
string: str = 'X'
number: int = 5
# 1: define function
def multiply_str(s: str, n: int) -> str:
    return s * n
output = multiply_str(string, number)
print(output)

# 2: create callable with lambda
multiply_str2: Callable[[str, int], str] = lambda s, n: s * n
output: Iterator[str] = multiply_str2(string, number)
print(list(output))

# 3: use lambda in-line
data: list[tuple[str, int]] = [('Bob', 3), ('X', 5), ('Python', 2)]
sm: Iterator[str] = starmap(lambda s, n: s * n, data)
print(list(sm))


# EXAMPLE 4:
(lambda s: print(f'{(s*3).capitalize()}!!!'))('Yo') # called on the spot
display_list: Callable[[list], None] = lambda l: print(*l, sep=', ', end='.\n') # returns nothing
display_list([1,2,3])