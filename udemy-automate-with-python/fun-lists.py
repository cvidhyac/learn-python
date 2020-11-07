for i in range(5):
  print(i)

# convert a range to list
print(list(range(4)))

# Count by 3 from 3 and print sequence up to 100
print(list(range(3, 100, 3)))

# Print index and value of a list
supplies = ['pen', 'pencil', 'crayons', 'markers', 'toys']
for item in range(len(supplies)):
    print('The item in position ' + str(i) + ' is : ' + supplies[i])

# Python multiple assignment avoids multiple lines of code
cat = ['loud', 'fat', 'orange']
sound, size, color = cat
print(sound)
print(size)
print(color)

## Multiple assignment to multiple values

size, color = 'thin',  'Yellow'
print(size)
print(color)

