# For explicit error handling
try:
    if 'x' in input('Do not type an x.'):
        raise RuntimeError('You typed an x.')        
except Exception as exc:
    print(exc)
else:
    print('You did not type an x.')
finally:
    print('Good Bye')

# Context managers: implicit error handling for resources:
with open('story.txt', 'w') as story:
    print('Once upon a time...', file=story)