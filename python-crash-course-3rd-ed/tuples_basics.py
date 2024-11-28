def tuples_basics():
    a_tuple = (100, 200, 200, 200)
    print(a_tuple)
    print(f"Number of occurrences of 200: {a_tuple.count(200)}")
    another_tuple = tuple(num for num in range(1, 10))
    print(another_tuple)
    as_a_list = list(another_tuple)
    as_a_list.append(100)
    print(f"Convert Tuple to list and print with additional element: {as_a_list}")


if __name__ == '__main__':
    tuples_basics()
