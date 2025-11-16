def tuples_basics():
    a_tuple = (100, 200, 200, 200)
    print(a_tuple)
    print(f"Number of occurrences of 200: {a_tuple.count(200)}")
    another_tuple = tuple(num for num in range(1, 10))
    print(another_tuple)
    as_a_list = list(another_tuple)
    as_a_list.append(100)
    print(f"Convert Tuple to list and print with additional element: {as_a_list}")

"""
Zip merges to lists and internally maintains them as tuple pairs
"""
def zip_example() -> None:
    list_one = ['John', 'Alice']
    list_two = ['Doe', 'King']
    zipped_object = zip(list_one, list_two)
    for item in zipped_object:
        print(f"The item of zipped object is of type {type(item)}, value: {item}")
        print(f"Value of item has a Key: {item[0]} and a value: {item[1]}")

if __name__ == '__main__':
    tuples_basics()
    print("Next is an example of zip")
    zip_example()