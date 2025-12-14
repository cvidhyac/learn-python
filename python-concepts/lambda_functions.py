import functools


def demo_named_lambda(value_one: int, value_two: int) -> None:
    """
    Lambda functions can be named or unnamed
    They should always be a single line of code that accepts input and returns output
    """
    cube = lambda x: x * x * x
    print(cube(value_one))

    sum_of_two = lambda x, y: x + y
    print(sum_of_two(value_one, value_two))

    parity = lambda x: 'odd' if x % 2 else 'even'
    print(parity(value_one))


def demo_lambda_nesting():
    higher_order_function = lambda l, func: func(sum(l))
    print(higher_order_function([1, 2, 3], lambda x: x * x))


def another_nested_lambda(shape: str, input_num: int) -> None:
    """
    Lambda functions can be nested
    """
    get_shape_area = lambda shape_area: (lambda x: x * x * 3.14) if shape == 'circle' else (lambda side: side * side)
    print(get_shape_area(shape)(input_num))


def demo_applying_lambda_using_map() -> None:
    """
    Map Takes a function and iterable and applies the function on each element of the iterable
    Returns a MapIterable which can be collected into a list/ set/ tuple of type iterable
    """
    an_iterable = [x * x for x in range(0, 10)]
    final_map = map(lambda x: x + 1, an_iterable)
    print(list(final_map))


def demo_applying_lambda_using_filter() -> None:
    """
    Filter takes an iterable and removes elements that don't match given condition
    Returns a Filtered Iterable which can be collected into a list/set or type of iterable
    """
    an_iterable = tuple(x for x in range(0, 25))
    filtered_list_of_even_nums = list(filter(lambda x: x % 2 == 0, an_iterable))
    print(f"List of filtered even nums {filtered_list_of_even_nums}")
    filtered_list_of_odd_nums = list(filter(lambda x: x% 2 !=0, an_iterable))
    print(f"List of filtered odd nums {filtered_list_of_odd_nums}")


def demo_reduce_functools(an_iterable: list) -> None:
    """
    Reduce is used from functools module. It reduces a given iterable to single value
    return one value
    """
    reduced_value = functools.reduce(lambda prev_val, curr_val: prev_val + 1 if curr_val % 2 else prev_val, an_iterable)
    print(reduced_value)

def demo_any_all(an_iterable: list) -> None:

    is_any_even = any(lambda x: x % 2 ==0 for x in an_iterable)
    print(is_any_even)

    is_all_odd = all(lambda x: x %2 != 0 for x in an_iterable)
    print(is_all_odd)

if __name__ == '__main__':
    demo_named_lambda(value_one=4, value_two=5)
    another_nested_lambda('square', 5)
    demo_applying_lambda_using_map()
    demo_applying_lambda_using_filter()
    demo_reduce_functools(an_iterable=[4, 9, 7])
    demo_any_all(an_iterable=[4, 9, 7])