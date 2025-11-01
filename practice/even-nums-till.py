
"""
The goal of function is to print even numbers till in two ways
1. using skip counting in for loop construct
2. Demonstrate same thing in while loop

Example:
    print_even_nums_till(10)
    0 2 4 6 8 10
"""
def print_even_nums_till() -> None:
    num = int(input("Enter a number till even number should be printed: "))
    for i in range(0, num, 2):
        print(i, end=" ")

    init_val = 0
    nums = []
    print("Now repeat using while loop .. ")
    while init_val <= num:
        if(init_val % 2) == 0:
            nums.append(init_val)
        init_val = init_val + 1
    nums.reverse()
    print(nums, end=" ")