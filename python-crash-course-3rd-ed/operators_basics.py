"""
There are 4 types of operators:
- Arithmetic
- Bitwise
- Relational operators
- membership operators
"""

def is_a_member(given_input:str, member_to_be_checked:str) -> bool:
    return member_to_be_checked in given_input

def not_a_member(given_input:str, member_to_check:str) -> bool:
    return member_to_check not in given_input

if __name__ == '__main__':
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