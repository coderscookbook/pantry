# Over sets or until termination:
for name in ['John', 'Fred', 'Bob']:
    if name.startswith('F'):
        continue
    print(name)

while input ('Stop') != 'stop':
    if 'x' in input('Do not type an x.'):
        print('You typed an x.')
        break
else:
    print('Loop finished without typing an x.')