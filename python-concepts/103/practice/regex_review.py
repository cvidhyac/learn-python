"""
Regex is useful in many cases - pattern matching, sometimes transforming a string from one to another
There are many repositories that help create regex patterns, so we rarely have the need to create our own regex.

Even while using a generated regex, understanding why it works is important to cover for edge cases.
Patterns are matched in order, even if same characters are present but order is incorrect, False will be returned.
"""
# [] {} () \ $ ^ + . ? | * are the regex meta characters
import re

def demo_capture_subgroups():
    person_and_email = "John Doe, email: john_doe@gmail.com"
    pattern = re.compile(r"([A-z][a-z]+ [A-z][a-z]+), email: ([a-z_0-9]+@[a-z]+\.[a-z]+)")
    name, email = re.search(pattern, person_and_email).groups()
    print(f"After capturing subgroups: {name}, email: {email}")

    a_math_expression = "10 + 5"
    pattern = re.compile(r"(\d+) ([+\-*/]) (\d+)")
    op1, operand, op2 = re.search(pattern, a_math_expression).groups()
    print(f"The value of op1 is: {op1}, operand is: {operand}, and final op2 is: {op2}")


def demo_find_iter():
    text = """
    Contact List:
        John Doe - 555-123-4567
        Jane Smith - (555) 987-6543
        Support Line - 555.222.1111
        Emergency Hotline: +1-555-444-8899
    """
    search_result = re.finditer(r'[+()\d{1}\s]?\d{3}[-.()\s]\d{3}[()-.\s]\d{4}', text)
    print(search_result)
    for num in search_result:
        print(f"Extracted phone number from finditer is : {num.group(0)}")

def demo_find_all_using_regex():
    """
    By default, the match functions return only one group of exact string match. Find all allows to return an
    array of matches present in the string.for example - extract all the phone numbers from given text
    :return: None
    """
    text = """
    Contact List:
        John Doe - 555-123-4567
        Jane Smith - (555) 987-6543
        Support Line - 555.222.1111
        Emergency Hotline: +1-555-444-8899
    """
    re_expression = r'[+\(\)]?\d{3}[-.\(\)\s]\d{3}[-.\s]\d{4}'
    result = re.findall(re_expression, text)
    print(result)

def demo_search_begins_with_ends_with():
    string_to_search = "Learning Python is fun"
    print(f"is_match_at_beginning: {re.search(r"^fun", string_to_search)}")
    print(f"is_match_at_end: {re.search(r'fun$', string_to_search).group(0)}")

def demo_split_using_regex():
    """
    Split string using regex pattern matching using the re.split function
    When `re.maxsplit` attribute is not specified exact string is returned, else a list is returned
    :return:
    """
    string_to_split = "Student 1: 89, 90, 91"
    split_result = re.split(r": ", string_to_split)
    print(split_result)
    another_string = "123$$$Main$$$Street"
    split_result = re.split(r"\$+", another_string)
    print(split_result)

def demo_substitute_using_regex():
    """
    sub method in regex pattern matching offers substitution feature, optional count can be specified to limit where
    this should be replaced. It creates a new string
    :return:
    """
    string_to_replace = "Apple\tBanana\tOrange\tCherry"
    replaced_string = re.sub(r'\t', ',', string_to_replace, count=1)
    print(replaced_string)

def search_using_regex_first_occurrence():
    """
    Difference between search and match - `match` only looks for matches at the beginning of the string whereas
    `search` looks for matches anywhere in the string
    :return:
    """
    string_to_search = "Student 1: 89, 90, 91"
    is_found:re.Match = re.search(r"\d+", string_to_search)
    print(is_found.group(0))
    another_string = "Learning Python is fun!"
    is_found:re.Match = re.search(r"Python", another_string)
    if is_found:
        print(f"Match found for pattern Python: {True}")
    else:
        print(f"Match found for pattern Python: {False}")

def search_case_insensitive():
    string_to_search = "Learning Python is fun!"
    is_found:re.Match = re.search(r"IS", string_to_search, flags=re.IGNORECASE)
    if is_found:
        print(f"Match found for pattern IS: {True}")
    else:
        print(f"Match found for pattern IS: {False}")

def demo_regex_meta_quantifier():
    print(
        f"string_to_match starts with either upper or lower case: {has_a_match('[A-Za-z][a-z]', "the employee joined the company on ")}")
    print(
        f"string_to_match starts with one upper case optionally followed by lower case : {has_a_match('[A-z][a-z]*', "W")}")
    print(
        f"string_to_match starts with at least one upper case, at least one lower case {has_a_match('[A-Z]+[a-z]+', "We")}")
    print(f"string_to_match has 0 or 1 occurrence preceding : {has_a_match('[A-Za-z]+[0-9]+[_-]?', "we99-")}")
    print(f"string_to_match has at least N occurrences: {has_a_match(r'[a-z]*\d{3,}', 'we999')}")
    print(f"string_to_match has between S to N occurrences: {has_a_match(r'[a-z]+\d{3,6}', 'we9955')}")
    print(f"string_to_match matches custom expression: {has_a_match(r'\d+ [A-za-z]+ [A-za-z]*', '123 Main St')}")


def has_a_match(pattern, text) -> bool:
    match:re.Match = re.match(pattern, text)
    if match is None:
        return False
    if match or match.group(0):
        return True
    else:
        return False


def intro_to_regex_metacharacters():
    """
    Regex becomes powerful when we start using its meta characters to create expressions
    r = raw string
    :return:
    """
    the_digits = re.match(r"\d{6}", "052210 is contained in string")
    print(f"The digits extracted : {the_digits.group(0) if the_digits else 'Invalid'}")


def regex_match_fixed_pattern_full_match(pattern, text):
    """
    Full match only returns true if entire string matches pattern
    :param pattern:
    :param text:
    :return:
    """
    match = re.fullmatch(pattern, text)
    if match:
        print(f"RegEx match successful: {match.group(0)}")
    else:
        print(f"No match for pattern: {pattern}")


def regex_match_specify_fixed_pattern(pattern, text):
    """
    re.match finds pattern at start of the string and returns true if pattern matches even if rest of the string doesn't match
    :param pattern: the pattern to match
    :param text: the entire text to match
    :return: None
    """
    match = re.match(pattern, text)
    if match:
        print(f"RegEx match successful: {match.group(0)}")
    else:
        print(f"No match for pattern: {pattern}")


if __name__ == '__main__':
    regex_match_specify_fixed_pattern('20250101', "the employee joined the company on 20250101")
    regex_match_specify_fixed_pattern('20250101', "20250101 is the date the employee joined the company")
    regex_match_fixed_pattern_full_match("the employee joined the company on ", "the employee joined the company on ")
    intro_to_regex_metacharacters()
    demo_regex_meta_quantifier()
    demo_substitute_using_regex()
    demo_split_using_regex()
    search_using_regex_first_occurrence()
    search_case_insensitive()
    demo_search_begins_with_ends_with()
    demo_find_all_using_regex()
    demo_find_iter()
    demo_capture_subgroups()