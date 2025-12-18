## Dictionaries example
myCat = {'size': 'fat', 'color': 'orange', 'sound': 'loud'}
print(myCat)

print('My cat has ' + myCat['color'] + ' fur')

## dictionaries are unordered
eggs = {'name': 'Sophie', 'species': 'cat', 'age': 8}
ham = {'name': 'Sophie', 'age': 8, 'species': 'cat'}
print(eggs == ham) ## prints true because dictionaries are unordered

## Dictionary important methods
print(eggs.keys())
print(eggs.values())

for k in eggs.keys():
  print(k)

#Print as tuples
for k, v in eggs.items():
  print(k, v)

## Exist condition for dictionaries

if 'color' in eggs:
  print('Exists')
elif 'color' not in eggs:
  print('Not Exists')
else:
  print('Undefined')

## Set default to ensure key exists
eggs.setdefault('color', 'black')
print(eggs)
eggs.setdefault('color', 'orange')
print(eggs) ## notice it does not change color because it already exists


