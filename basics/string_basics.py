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


if __name__ == '__main__':
    use_fstring()
    use_string_case()
    use_string_whitespace_methods()
    use_prefix_methods()
