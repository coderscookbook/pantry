from itertools import permutations
list = [1, 2, 3]
p = permutations(list)  # (list, r=2) --> r tells how long the perms are
print(list(p))          # prints all possible permutations