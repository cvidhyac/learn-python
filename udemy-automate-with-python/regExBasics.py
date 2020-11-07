import re


# If we want to check if a specific regEx String contains a specific phone numbr
# as pattern
def simple_regular_expression(text_message):
  phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
  match_found = phone_regex.search(text_message)
  # Group prints first occurrence
  print(match_found.group())


def group_example(text_message):
  group_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')
  match_found = group_regex.search(text_message)
  print(match_found.group(2))


# The \d indicates a digit
def regex_escape_example(text_pattern):
  escape_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d)-\d\d\d')
  match_found = escape_regex.search(text_pattern)
  print(match_found.group(1))


# Pipe character defines one of many possible groups
def regex_multiple_options(text_pattern):
  multiple_options_regex = re.compile(r'bat(man|woman|mobile)')

  match_found = multiple_options_regex.search(text_pattern)
  print(match_found.group())

  # Print all the matches
  for match in re.finditer(multiple_options_regex, text_pattern):
    the_value = match.group()
    the_suffix_where_it_was_found = match.group(1)
    print("The value is : " + the_value + " matched against pattern-suffix : "
          + the_suffix_where_it_was_found)


## Demo time!

simple_regular_expression("Please contact the listed phone number 123-456-789")
group_example(
    "Please check occurences for 123-456-789 and verify 456 is printed")
regex_escape_example("I want to print with paranethesis - (678)-456-789")
regex_multiple_options('''The batman toy is a package comprising of batman,
                       batwoman, a batmobile and a batcopter. Kids enjoy
                       playing with all the bat toys very much''')
