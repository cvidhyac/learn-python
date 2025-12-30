import pandas as pd
import re


def find_five_digit_zipcodes():
    """
    Pandas Series `str` accepts regex patterns to evaluate each item in a series
    :return:
    """
    zips = pd.Series({
        "Boston": "223356",
        "Raleigh": "22320",
        "Atlanta": "2233"
    })
    zips_with_match = zips.str.match(r'\d{5}$')
    print(zips_with_match)


def check_string_contains_a_pattern():
    """
    Match looks for match, however contains looks for partial match anywhere in the string
    :return:
    """
    cities = ['Boston, MA 2200', 'Raleigh, NC 33001', 'Atlanta, GA 55234', 'San Francisco, CA', "Texas", "226707"]
    zips = pd.Series(cities)
    patterns = re.compile(r'[A-Z][a-z]+')
    zips_contain_pattern = zips.str.contains(patterns)
    print(zips_contain_pattern)


def _get_formatted_phone(phone) -> str:
    pattern = re.compile(r'(\d{3})(\d{3})(\d{4})')
    result = re.fullmatch(pattern, str(phone))
    if result:
        part_one, part_two, part_three = result.groups()
        formatted_result = "(" + part_one + ") " + "-".join([part_two, part_three])
        return formatted_result
    else:
        return phone



def apply_regex_on_dataframes():
    contacts = [
        ["Mike", "300", "mk@hotmail.com", 5556666789],
        ["Jane", "500.00", "jk@aol.com", 2223334567]
    ]
    contacts_df = pd.DataFrame(contacts, columns=["name", "salary", "email", "phone"])
    formatted_phone = contacts_df["phone"].map(_get_formatted_phone)
    contacts_df["phone"] = formatted_phone
    print(contacts_df)






if __name__ == '__main__':
    find_five_digit_zipcodes()
    check_string_contains_a_pattern()
    apply_regex_on_dataframes()