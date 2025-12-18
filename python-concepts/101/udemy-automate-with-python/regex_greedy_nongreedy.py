## Usage of ?, * and +
# ? = Optional : zero or one, None returned if no match found
# * = At least one occurrence
# + = One or more occurrences
# {N} = Specific number of times
# {N, N} = denotes the number of matches (min, up-to-max)

# What is greedy match in regex? Goes for longest possible number to match
# What is non-greedy match ? Goes for the smallest number to match
# By default RegEx matching is a greedy match

import re


def regex_optional_occurrence(text_pattern):
  optional_occurrence_regex = re.compile(r'bat?(wo)man')
  for match in re.finditer(optional_occurrence_regex, text_pattern):
    print("The occurence is : " + match.group())

# Matches both batman and batwoman
def regex_zero_or_more(text_pattern):
  zero_or_more_regex = re.compile(r'bat(wo)*man')
  for match in re.finditer(zero_or_more_regex, text_pattern):
    print("Atleast one Match found at : " + match.group())

# Matches only batwoman, batman is not matched
def regEx_one_or_more(text_pattern):
  one_or_more_regex = re.compile(r'bat(wo)+man')
  for match in re.finditer(one_or_more_regex, text_pattern):
    print("One or more Match found for : " + match.group())

## Specific number of repetitions
def count_repetitions(text_pattern):
  repeat_regex = re.compile(r'(Ha){3}')
  match_found = repeat_regex.search(text_pattern)
  print("Repeat match found at : " + match_found.group())

# Upper bound is used in greedy match
def greedy_match(text_pattern):
  greedy_regex = re.compile(r'(\d){3,5}')
  match_found = greedy_regex.search(text_pattern)
  print("The lucky number is : " + match_found.group())

# Lower bound is used in non-greedy match
def non_greedy_match(text_pattern):
  non_greedy_regex = re.compile(r'(\d){3,5}?')
  match_found = non_greedy_regex.search(text_pattern)
  print("The lucky number is : " + match_found.group())

## Demo time

regex_optional_occurrence("We found a batwoman and a batman")
regex_zero_or_more("Can you find batwowowowowowoman and batman ?")
regEx_one_or_more("Can you find batwowowowowowoman and batman ?")


### repetitions
count_repetitions("Ha Ha Ha hahahahah HaHaHa")
greedy_match('''How many digits are printed in 99999999''')
non_greedy_match('''How many digits are printed in 99999999''')

