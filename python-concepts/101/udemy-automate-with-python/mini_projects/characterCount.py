import pprint

message = 'It was a bright sunny day where sun shines really bright and everything ' \
          'was so lovely.'

multiLineMessage = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'''

count = {}
for character in multiLineMessage:
  count.setdefault(character, 0)
  count[character] = count[character] + 1

print(count)

##pretty print
pprint.pprint(count)

#Store the value of formatted text to a variable as string
formattedText = pprint.pformat(count)
print(formattedText)
