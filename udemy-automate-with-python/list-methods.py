#List Methods
input = ['hello', 'world', 'hey', 'hyalo']
print(input.index('world'))

#Append end of list
input.append('pooka')
print(input)

#Insert at specific position
input.insert(1, 'chicken')
print(input)

#Remove element from list
input.remove('chicken')
print(input)

#Delete an element from index
del input[0]
print(input)

#Sort the list, default ascending
input.sort()
print(input)

#Sort the list with reverse
input.sort(reverse=True)
print(input)

#Sort the true alphabetical sorting
names = ['Alice', 'key', 'Key', 'Bob', 'bob']
names.sort(key=str.lower)
print(names)
