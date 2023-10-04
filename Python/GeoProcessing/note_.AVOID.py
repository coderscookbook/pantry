#1
a = [1, 2, 3]
# wrong
for a in a: #creates 'a' as variable instead of keeping list
    print(a)
print(a)    #prints last value it grabbed instead of list
a.append(4) #creates AttributeError
# correct
for num in a:
    print(a)
a.append(4)
print(a)    #prints list 1,2,3,4

