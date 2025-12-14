
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

if __name__ == '__main__':
    demo_list_comprehension()
    demo_set_comprehension()
    demo_dict_comprehension()