def use_fstring():
    first_name = 'first'
    last_name = 'doe'
    print("---------")
    print(f"Hello {first_name} {last_name}")


def use_string_case():
    test_string = "Change me"
    as_upper = test_string.upper()
    as_lower = test_string.lower()
    as_title = test_string.title()
    print("---------")
    print(f"{as_upper}\n{as_lower}\n{as_title}")


def use_string_whitespace_methods():
    test_string = "       content        "
    no_right_space = test_string.rstrip()
    no_left_space = test_string.lstrip()
    all_space = test_string.strip()
    print("---------")
    print(f"{no_right_space}\n{no_left_space}\n{all_space}")


def use_prefix_methods():
    test_string_one = "Mr. John Doe".removeprefix("Mr.").strip()
    test_string_two = "Jane Doe Jr.".removesuffix("Jr.").strip()
    print("---------")
    print(f"{test_string_one}\t{test_string_two}")

def get_formatted_name(first_name:str, last_name:str):
    if len(first_name.strip()) <= 0:
        raise ValueError("First name is empty")
    elif len(last_name.strip()) <=0:
        raise ValueError("Last name is empty")
    else:
        return f"{first_name} {last_name}".title()

def slicing_a_string(value:str) -> None:
    sliced_value = value[:4:-1]
    print(f"last 4 characters of string : {value} is : {sliced_value}")

def find_substring_at_index(value:str, substr:str) -> None:
    print(f"The substring presence in index: {value.find(substr)}")

def reverse_using_slicing(value:str) -> None:
    reversed_value = value[::-1]
    print(f"reversed value {reversed_value}")

"""
The purpose of find and index is very similar. Both are used for finding if a given substring is present or not.
However, find returns `-1` when string is not found however index method throws exception. So depending on use case
if scenario is error or negative validation check, one of them could be used as needed.
"""
def find_and_index_methods(value:str, substr:str) -> None:
    try:
        print(f"The substring {substr} is not present in given string: {value.find(substr)}")
        print(f"Now try again by using index method instead: {value.index(substr)}")
    except ValueError:
        print(f"Substring {substr} not found is caught as Value Error for given input string {value}")

if __name__ == '__main__':
    use_fstring()
    use_string_case()
    use_string_whitespace_methods()
    use_prefix_methods()
    slicing_a_string("pineapple")
    find_substring_at_index("pineapple", "eap")
    reverse_using_slicing("pineapple")
    find_and_index_methods("pineapple", "orange")