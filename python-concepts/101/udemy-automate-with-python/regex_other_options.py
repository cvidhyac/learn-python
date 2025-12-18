# findAll - return a list when there is zero or ONE groups
# findAll - returns a list of tuples when there is two or more groups
# [] - Custom character class
# Use {} to specify occurrence in a patterns - {2} -> two vowels 'ao'in a row
# ------------------------------
# Caret has two behaviours : when within character class, it performs negate
# Caret at beginning
# [^ ] - Negate condition
# Caret (^) at the beginning of regEx means "starts With"
# Dollar($) at the end of the regEx means "Ends With"
# Presence of both Caret(^) and Dollar($) indicates "Exact match

import re


def find_all_as_a_list(text_pattern):
  find_regex = re.compile(r'\d{3}')
  list_match = find_regex.findall(text_pattern)
  print(list_match)


def find_all_as_tuples(text_pattern):
  find_tuple_regex = re.compile(r'(\d)-(\d\d)-(\d\d\d)')
  tuple_match = find_tuple_regex.findall(text_pattern)
  print(tuple_match)


def custom_class_find_vowels(text_pattern):
  custom_regex = re.compile(r'[aeiouAEIOU]{2}')
  list_of_matches = custom_regex.findall(text_pattern)
  print(list_of_matches)


def custom_class_alphabet_seq(text_pattern):
  custom_alpha = re.compile(r'[a-f]')
  list_of_matches = custom_alpha.findall(text_pattern)
  print(list_of_matches)

  ## Print negation using Caret(^)
  custom_does_not_contain = re.compile(r'[^a-f]')
  list_of_does_not_contain = custom_does_not_contain.findall(text_pattern)
  print(list_of_does_not_contain)

def find_exact_match(text_pattern):
  exact_match_regex = re.compile(r'^Hello\sWorld$')
  match_found = exact_match_regex.search(text_pattern)
  if match_found != None:
    print(match_found.group())
  else:
    print("No Match found!")

def all_digits(text_pattern):
  all_digits_regex = re.compile(r'^\d+$')
  match_found = all_digits_regex.search(text_pattern)
  print(match_found.group())

def find_words_that_contain(text_pattern):
  find_words_regex = re.compile(r'.at')
  word_list = find_words_regex.findall(text_pattern)
  print(word_list)

  whole_words_regex = re.compile(r'.{1,2}at')
  whole_word_list = whole_words_regex.findall(text_pattern)
  print(whole_word_list)


## Demo time!!
find_all_as_a_list("The three musketeers : 1022, 303, 678 and 890")
find_all_as_tuples(
  "The number pattern goes like this : 1-12-123, 2-23-234, 3-34-345")
custom_class_find_vowels(
  "The string will print vowels in umbrella And EGG plus chicken coop")
custom_class_alphabet_seq(
  "The alphabet sequence has many permutations and combinations")
find_exact_match("Hello World")
all_digits("123456788")
find_words_that_contain("The cat in the hat lost his flat and he sat on a mat")