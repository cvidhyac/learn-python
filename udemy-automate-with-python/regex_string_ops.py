## Using RegEx for character extraction
# By default .* matches everything but new line. Once it encounters \n it stops.
# To override, specify re.DOTALL parameter
# Case Insensitive matching -  re.IGNORECASE
# find and replace OR Substitution - sub()
# Use verbose mode to use comments within regex to explain complex ones
# You can use bitwise OR operator | to combine muliple regexp arguments

import re


def find_elements(text_pattern):
  # Greedy find to extract data
  elements_regex = re.compile(r'FirstName: (.*) LastName: (.*)')
  collected_data = elements_regex.findall(text_pattern)
  print(collected_data)


def find_html_tags(text_pattern):
  # non-greedy find to extract data
  non_greedy_elements_regex = re.compile(r'<(.*?)>')
  collected_data = non_greedy_elements_regex.findall(text_pattern)
  print(collected_data)


def demo_dot_all(text_pattern):
  # Without dot all, notice it stops at first line of provided text
  default_dotstar_regex = re.compile(r'.*')
  default_match_found = default_dotstar_regex.search(text_pattern)
  print(default_match_found.group())

  dot_all_regex = re.compile(r'.*', re.DOTALL)
  match_found = dot_all_regex.search(text_pattern)
  print(match_found.group())


def case_insensitive(text_pattern):
  case_insensitive_regex = re.compile(r'[a-z]', re.IGNORECASE)
  match_found_list = case_insensitive_regex.findall(text_pattern)
  print(match_found_list)


def substitution(text_pattern):
  substitution_regex = re.compile(r'Agent \w+')
  new_string = substitution_regex.sub('REDACTED', text_pattern)
  print(new_string)


def sensitive_data_mask(text_pattern):
  pii_mask_regex = re.compile(r'email : (\w)(\w*)')
  masked_string = pii_mask_regex.sub('email : \1********', text_pattern)
  print(masked_string)


def readable_regex_with_bitwise_operator(text_pattern):
  readable_regexp = re.compile(r'''
  \d\d\d- #This represents the optional area code
  \d\d\d-\d\d\d\d #This represents the actual number of the person
  ''', re.VERBOSE | re.DOTALL | re.IGNORECASE)
  match_found = readable_regexp.search(text_pattern)
  print(match_found.group())


## Demo Time!!
find_elements("FirstName: John LastName: Doe")
find_html_tags("<h1> Title </h1> <h2> Table of contents </h2>")
demo_dot_all("This is prime.\nThis is even.\nThis is odd.\n")
case_insensitive("Hello World, india and other Continents")
substitution("Agent Bob gave secret documents to Agent Alice")
sensitive_data_mask("You enrolled with us using email : johndoe@gmail.com")
readable_regex_with_bitwise_operator("Find my phone number : 678-123-1233")
