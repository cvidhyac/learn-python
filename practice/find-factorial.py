
"""
Find factorial of given number
5! = 5 * 4* 3 * 2 * 1 = 120
"""

def find_factorial():
    num = int(input())
    fact = 1
    count = 1
    while count <= num:
        fact = fact * count
        count = count + 1
    print(f"the factorial is: {fact}")

"""
Find sum of digits
123 = 1 + 2 + 3 = 6
"""
def find_sum_of_digits():
    num = 45678
    sum_of_digits = 0
    while num != 0:
        sum_of_digits = sum_of_digits + (num % 10)
        num = num // 10

    print(sum_of_digits)