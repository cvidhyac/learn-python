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