def for_loop_using_list_comprehension():
    nums = [value for value in range(1, 10)]
    print(nums)

def simple_for_loop():
    my_items = ["Pen", "Pencil", "Paper", "Strings"]
    print(f"Size of my pencil box items - {len(my_items)}")
    for item in my_items:
        print(f"Current item - {item}")

def a_number_loop():
    compiled_nums = [value**2+value for value in range(1, 1000)]
    print(compiled_nums)

def find_squares():
    squares = []
    for val in range(1, 11):
        squares.append(val**2)
    print(squares)

def find_squares_as_list_comprehension():
    squares = [val**2 for val in range(1, 11)]
    print(f'As list comprehension {squares}')

def sum_of_a_million():
    a_million_nums = [num for num in range(1, 1000_000)]
    print(sum(a_million_nums))

def use_max_and_min():
    a_million_nums = [num for num in range(1, 1_000_000)]
    print(f"Max of a million : {max(a_million_nums)}")
    print(f"Min of a million : {min(a_million_nums)}")

def find_odd_numbers():
    odd_nums = [num for num in range(1, 20, 2)]
    print(f"List of odd numbers : {odd_nums}")

def find_cubes():
    cube = [num**3 for num in range(1, 10)]
    print(f"List of ten cubes: {cube}")

def find_multiples_of_three():
    multiples_of_3 = [val for val in range(3, 31, 3)]
    print(multiples_of_3)


def find_first_three_players():
    players = ["A", "D", "Z", "K", "L", "M"]
    print(f"First 3 players: {[player for player in players[0:3]]}")

def example_for_while_loop():
    i = 0
    multiples_of_five = []
    while i <= 100:
        if i % 5 == 0:
            multiples_of_five.append(i)
            i = i + 5
    else: # the else condition in a while loop only executes if there was no usage of 'break' statement and condition was false
        print(f"The list of multiples of five till 100 are : {multiples_of_five}")

def example_of_continue():

    i = 0
    while True:
        if i > 100:
            print()
            print("Exit program")
            break
        if i % 7 == 0:
            print(i, end=" ")
            i = i + 7
            continue
        i = i + 1

"""
Brute force solution to print triangles
Space complexity - O(1), no extra storage
Time complexity:
- Outer loop runs n-1 times = n
- Inner loop runs n-1 times = n
Total time complexity: O(n^2), not good
"""
def print_triangles(num: int) -> None:
    i = num - 1 # 4
    while i >= 1: # 4 >=1
        j = 1
        print_val = num - i
        while j <= print_val:
            print(print_val, end="")
            j = j + 1
        print()
        i = i - 1

def print_triangles_with_string_repetition():
    num = int(input("Enter number of triangles to be printed: "))
    for i in range(1, num):
        print(i * str(i))

if __name__ == '__main__':
    for_loop_using_list_comprehension()
    simple_for_loop()
    a_number_loop()
    find_squares()
    find_squares_as_list_comprehension()
    sum_of_a_million()
    use_max_and_min()
    find_odd_numbers()
    find_cubes()
    find_multiples_of_three()
    find_first_three_players()
    example_for_while_loop()
    example_of_continue()
    print_triangles(5)
    print_triangles_with_string_repetition()