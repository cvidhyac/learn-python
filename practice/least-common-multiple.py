"""
Follows the same mathematical relationship from GCD. If you are good at GCD, LCM is going to be easy.

To find LCM, find the GCD first. Then, use the formula = (a * b) / gcd (a, b) to find LCM.
For GCD, we will use the Euclid's algorithm with modulo method and tuple unpacking.
"""
import functools


def find_gcd(num_one:int, num_two:int) -> int|None:
    # arrange numbers so that first number is always greater
    if num_two > num_one:
        num_one, num_two = num_two, num_one

    while num_two != 0:
        print(f"run gcd({num_one},{num_two})")
        num_one, num_two = num_two, num_one % num_two

    if num_two == 0:
        return num_one

def find_lcm(num_one:int, num_two:int) -> int:

    gcd = find_gcd(num_one, num_two)
    print(f"The GCD of {num_one} and {num_two} is {gcd}")

    lcm = abs(num_one * num_two) // gcd
    print(f"The LCM of {num_one} and {num_two} is {lcm}")
    return lcm

def lcm_of_numbers():
    nums = str(input("Enter numbers to find LCM separated by comma: "))
    nums_as_list = list(map(int, nums.strip().split(",")))
    lcm = functools.reduce(find_lcm, nums_as_list)
    print(f"The final LCM is {lcm}")

if __name__ == "__main__":
    lcm_of_numbers()


