"""
Regex is useful in many cases - pattern matching, sometimes transforming a string from one to another
There are many repositories that help create regex patterns, so we rarely have the need to create our own regex.

    Patterns are matched in order, even if same characters are present but order is incorrect, False will be returned.
"""
# [] {} () \ $ ^ + . ? | * are the regex meta characters
import re

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