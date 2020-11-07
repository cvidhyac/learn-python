import copy

# Strings are immutable

print(list('Hello'))

name = 'Sophie'
print(name[0])

# Create new string using slice
newName = name[0:3] + 'aft'
print(newName)

newList = ['Hello', 1, 2, 3, 4]
cheese = newList

## pass by reference, not pass by value
cheese[0] = 'R'
print(cheese)
print(
    newList)  # new list was also modified because its pass by reference in list

# Use Copy module to decouple from default behaviour of pass by reference
newCheeseList = copy.deepcopy(newList)  # Deepcopy creates a new list altogether
newCheeseList[1] = 'S'
print(newCheeseList)
print(newList)

## Line continuation in IDE for print

print('Hello' + \
      'World')
