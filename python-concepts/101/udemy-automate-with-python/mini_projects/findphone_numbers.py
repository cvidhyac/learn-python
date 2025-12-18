### Find 3 phone numbers where each phone number may or may not have an
# area code in the first 3 digits.

import re

def find_three_phone_numbers(text_pattern):
  phone_number_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d(,)?){3}')
  match_found = re.search(phone_number_regex, text_pattern)
  print("Match found : " + match_found.group())

find_three_phone_numbers("123-456-789,456-789,234-456")
