
"""
Find if given number is prime or not
"""

def find_prime_number():
    num = int(input("Enter a number to check for prime: "))
    number_of_factors = 0
    counter = 1
    while counter <= num:
        if(num % counter) == 0:
            number_of_factors = number_of_factors + 1
        counter = counter + 1
    if number_of_factors == 2:
        print(f"Number {num} is a prime number")
    else:
        print(f"Number {num} is not a prime number")
