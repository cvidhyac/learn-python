from functools import reduce

""""
Higher order functions: A function that takes another function as input
It helps us imagine another function as a container and helps develop abstractions
"""


def prod_of_digits(n: int) -> int:
    product = 1
    while n != 0:
        product = product * (n % 10)
        n = n // 10
    print(f"Final product: {product}")
    return product


def sum_of_prod_of_list(a_list: list, func) -> int:
    print(func, type(func))
    total = sum(a_list)  # adds all elements in list
    print(f"Sum of list: {total}")
    return func(total)


def demo_higher_order_functions():
    list_of_nums = [12, 13, 100, 91]
    ans = sum_of_prod_of_list(list_of_nums, prod_of_digits)
    print(f"The result of executing a higher order function is: {ans}")


def demo_map_filter_reduce():
    """
    Map and Filter are built-in functions, reduce belongs in functools
    :return:
    """
    list_of_nums = [12, 13, 100, 91]

    squared_list = list(map(lambda x: x ** 2, list_of_nums))
    print(type(squared_list))
    print(f"Example using map keyword: {squared_list}")

    filtered_list = list(filter(lambda x: x % 10 == 0, squared_list))
    print(f"Example using filtered_list {filtered_list}")

    reduced_value = reduce(lambda x, y: x * y, list_of_nums)
    print(f"Reduced value of list containing product of all elements: {reduced_value}")

    # convert given numbers to centigrade and map to list of tuples containing Fahrenheit and equivalent Celsius values
    list_of_three = [41, 32, 212]
    as_tuple_of_converted_vals = list(map(lambda fah: (fah, (fah - 32) * (5 / 9)), list_of_three))
    print(as_tuple_of_converted_vals)


if __name__ == '__main__':
    demo_higher_order_functions()
    demo_map_filter_reduce()
    demo_higher_order_functions()
