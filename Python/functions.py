'''WHAT NOT TO DO'''
def func(key, value, d={})
    d[key] = value
    print(d)

func('a', 10)
#prints {'a': 10}
func('b', 20)
#prints {'a': 10, 'b': 20}
#expected -> {'b', w20}t does