#  Use the standard regex classes to split the lyrics to a list

import re

def twelve_days_of_christmas(text_pattern):
  twelve_days_regex = re.compile(r'\d+\s\w+')
  list_of_matches = twelve_days_regex.findall(text_pattern)
  print(list_of_matches)



#--------------------------
# Demo Time!!

lyrics = '''
12 drummers drumming,
11 pipers piping,
10 lords a leaping,
9 ladies dancing,
8 maids a milking,
7 swans a swimming,
6 geeses a laying,
5 golden rings,
4 calling birds,
3 french hens,
2 turtle doves,
and 1 partridge in a pear tree
'''
twelve_days_of_christmas(lyrics)
