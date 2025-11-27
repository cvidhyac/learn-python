""""
Higher order functions: A function that takes another function as input
It helps us imagine another function as a container and helps develop abstractions
"""

def prod_of_digits(n:int) -> int:
    product = 1
    while n != 0:
        product = product * (n % 10)
        n = n // 10
    print(f"Final product: {product}")
    return product

def sum_of_prod_of_list(a_list:list, func) -> int:
    print(func, type(func))
    total = sum(a_list) # adds all elements in list
    print(f"Sum of list: {total}")
    return func(total)

def demo_higher_order_functions():
    list_of_nums = [12, 13, 100, 91]
    ans = sum_of_prod_of_list(list_of_nums, prod_of_digits)
    print(f"The result of executing a higher order function is: {ans}")

if __name__ == '__main__':
    demo_higher_order_functions()