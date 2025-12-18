from loop_basics import find_multiples_of_three


def demo_list_comprehension() -> None:
    an_iterable = [x * x for x in range(10)]
    print(an_iterable)

def demo_set_comprehension() -> None:
    an_iterable = { x ** 2 for x in range(10) }
    print(an_iterable)

def demo_dict_comprehension() -> None:
    list_one = ['Apple', 'Orange', 'Pineapple']
    list_two = [ 'Sauce', 'Juice', 'Salsa']
    combined_dict = { key : value for key, value in (zip(list_one, list_two)) } # How to create a map in python
    print(combined_dict)

def comprehension_with_generator_and_conditions():
    """
    Generators are comprehensions defined with parentheses, they are lazy evaluated hence offer better memory
    management for large volumes of data.
    :return:
    """
    list_nums = (x**2 for x in range(10, 20) if x % 2 == 0)
    print(type(list_nums))
    print(list(list_nums))

    another_example = [10, 3, 7, 1, 9, 4]
    cubes_of_example = (x**3 for x in another_example)
    print(list(f"Cubes of example using generator expressions: {cubes_of_example}"))

def comprehension_as_tuple() -> None:
    cubed_nums = [(index, value**3) for index, value in enumerate(range(10))]
    print(cubed_nums)

def comprehension_with_steps()  -> None:
    """
    List Generator expressions are greedy expressions, whereas the generator expressions are lazy evaluated
    Generator expressions offers better memory management and works nicely with comprehensions.
    :return:
    """
    multiples_of_three_and_six = list(x for x in range(3, 100, 3) if x % 3 ==0 and x % 6 == 0)
    print(multiples_of_three_and_six)


if __name__ == '__main__':
    demo_list_comprehension()
    demo_set_comprehension()
    demo_dict_comprehension()
    comprehension_with_generator_and_conditions()
    comprehension_as_tuple()
    comprehension_with_steps()