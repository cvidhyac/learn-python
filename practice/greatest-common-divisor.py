"""
Find the GCD of two given numbers
GCD = greatest common divisor

18 = 1, 2, 3, 6, 9, 18
54 = 1, 2, 3, 6, 9, 12, 18, 27, 54
"""
import functools

# ----------------- Brute force method -------------------

"""
The brute force method would be to find factors for each number, then identify common factors, then find largest one
Big O Analysis - 

Time Complexity - 0(n
Space complexity - upto O(n + m)
"""


def find_factors(num) -> list[int]:
    i = 1
    factors = []
    while i <= num:
        if num % i == 0:
            factors.append(i)
        i = i + 1
    return factors


def find_gcd(num_one, num_two) -> int:
    to_factors_num_one = set(find_factors(num_one))
    to_factors_num_two = set(find_factors(num_two))
    common_factors = [x for x in to_factors_num_one if x in to_factors_num_two]
    return max(common_factors)


# -------------------------- Euclid's algorithm --------------------

"""
Euclid's algorithm states that the gcd of a number doesn't change if the larger number is replaced by the remainder 
when dividing it by the smaller number.

Repeat until the remainder is 0, the GCD is the current b.

step    a       b       a % b   next(a, b)
1       54      18     54 % 18  (18, 0) ---> gcd is 18

1       60      36     60 % 36  (36, 24)
2       36      24     36 % 24  (24, 12)
3       24      12     24 % 12  (12, 0) ---> gcd is 12

gcd(36, 60) --> 12

Mathematical representation:

gcd(a, b) = gcd(b, a mod b) where a is higher than b
When b = 0, the gcd is a

54
"""


def gcd_by_euclids_algorithm(num_one, num_two) -> int:
    # swap numbers so that a becomes the greater number
    if num_two > num_one:
        num_one, num_two = num_two, num_one

    # recursion end condition
    if num_two == 0:
        return num_one
    else:
        num_one, num_two = num_two, num_one % num_two
        print(f" retry gcd({num_one}, {num_two}) ")
        return gcd_by_euclids_algorithm(num_one, num_two)


"""
The Tuple unpacking method covers the swapping without creation of a temp variable and is a clean pythonic way.
Under the hood python creates a temp tuple of current variables, then evaluates RHS side first and then assigns to LHS.

By using this, we optimize it from O(log n) to O(1) complexity.
"""


def gcd_by_euclids_algorithm_tuple_unpacking(num_one, num_two) -> int:
    # arrange numbers so that first number is always greater
    if num_two > num_one:
        num_one, num_two = num_two, num_one
    while num_two != 0:
        num_one, num_two = num_two, num_one % num_two
    return num_one


"""
    Quadratic complexity - brute force approach - O(N + M) space complexity 
    Scales moderately, simpler but still linear
"""


def option_one_quadratic_complexity_brute_force_approach(num_one, num_two):
    op = find_gcd(num_one, num_two)
    print(f"The greatest common divisor of {num_two} and {num_two} is {op}")


"""
    Euclids algorithm - implement using recursion
    Space complexity - O(log n) - Optimal and clean
"""


def option_two_euclids_algorithm_recursion_approach(num_one, num_two):
    op = gcd_by_euclids_algorithm(num_one, num_two)
    print(f"The greatest common divisor of {num_one} and {num_two} is {op}")


"""
    O(1) space complexity - Fastest and safest
"""


def option_three_euclids_algorithm_modulo_approach(num_one, num_two):
    op = gcd_by_euclids_algorithm_tuple_unpacking(num_one, num_two)
    print(f"The greatest common divisor of {num_one} and {num_two} is {op}")


"""
There are three approaches I have tried to find greatest common divisor:
- Brute force method
- Euclid's algorithm with recursion
- Euclid's algorithm with modulo iteration
"""


def approaches_to_find_gcd_for_one_number():
    first_num = int(input("Enter first number to find gcd: "))
    second_num = int(input("enter second number to find gcd: "))
    # option_one_quadratic_complexity_brute_force_approach(first_num, second_num)
    # option_two_euclids_algorithm_recursion_approach(first_num, second_num)
    option_three_euclids_algorithm_modulo_approach(first_num, second_num)


"""
Scaling the first approach to extend it for multiple numbers.
functools.reduce is great for mathematical operations where same operation needs to be rolled over to the rest
of the numbers. So gcd - f([a, b, c, d) becomes f((a, b), c), d)
"""


def gcd_for_multiple_numbers():
    numbers = str(input("Enter a list of comma separated numbers to find GCD: "))
    numbers_to_list = list(map(int, numbers.strip().split(",")))
    op = functools.reduce(gcd_by_euclids_algorithm_tuple_unpacking, numbers_to_list)
    print(f"The GCD of multiple numbers provided {numbers} is {op}")


if __name__ == "__main__":
    # approaches_to_find_gcd_for_one_number()
    gcd_for_multiple_numbers()
