input = ['cat', 'bat', 'mat']
print(input[0])
print(input[1])
multiArray = [['cat', 'bat'], [10, 20, 30]]
print(multiArray[0][1]) #prints bat
print(multiArray[1][0]) #prints 10

print(input[-1]) #refers last element in list
print(input[-2]) #refers to last but one element

print(input[0:2]) # slice evaluates to a new list

## Change list items
input[1]='hat'
print(input)

input[0:2] = ['sfffd', 'sdfsdf', 'ertert']
print(input)

print(input[1:]) #Everything starting AFTER from index position 1
print(input[:2]) #Everything starting BEFORE index position 2

del input[0] #Delete specific index position 0, unassignment statement
print(input)
print(len(input))

## list concatenation
print([1, 2, 3] + [4, 5, 6])

# Convert a string to array
print(list('Hello'))

## IN and NOT IN Operator prints boolean
print(42 in [1, 2, 3])
print(42 not in [1, 2, 3])
print('H' in ['H', '2', '3'])