"""
There are 4 types of operators:
- Arithmetic
- Bitwise
- Relational operators
- membership operators
- Identity operators
"""

def is_a_member(given_input:str, member_to_be_checked:str) -> bool:
    return member_to_be_checked in given_input

def not_a_member(given_input:str, member_to_check:str) -> bool:
    return member_to_check not in given_input

def identity_checker():

    # String is immutable data type
    s1 = "hello"
    s2 = "hello"
    is_string_id_same = s1 is s2

    # Print identity of where the string is stored
    print(f"The ID where s1 is stored is {id(s1)} and ID for s2 is {id(s2)}")

    tuple_one = (1, 2, 3)
    tuple_two = (1, 2, 3)
    is_tuple_id_same = tuple_one is tuple_two

    print(f"""When immutable types are used, they will be stored in same memory 
    location for String : {is_string_id_same} AND Tuple: {is_tuple_id_same}""")

    # List is mutable type
    list_one = [1, 2, 3]
    list_two = [1, 2, 3]
    print(f"""when type is not immutable, then same values are stored in different memory
     locations hence considered different values: {list_one is list_two}""")



def membership_checker():
    input_str = "pineapple"
    quit_flag = 's'
    while quit_flag != 'q':
        print("Enter member to be checked: ")
        member = str(input())
        has_member = is_a_member(input_str, member)
        print(f"The given input string {input_str} returned {has_member} for IN membership check")
        is_not_a_member = not_a_member(input_str, member)
        print(f"The given input string {input_str} returned {is_not_a_member} for NOT IN membership check")
        quit_flag = str(input("Type q to quit: "))


if __name__ == '__main__':
    #membership_checker()
    identity_checker()