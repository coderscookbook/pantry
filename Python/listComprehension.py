groups = [[1,2],[3,4]]

'''
#OLD WAY w/NESTED FOR LOOPS

for group in groups:
    for element in group:
        print(element, end='')
#output: 
'''

# New way
c = [element for group in groups for element in group]
print(c)
