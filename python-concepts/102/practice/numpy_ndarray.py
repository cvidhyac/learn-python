import numpy as np


def demo_ndarray_101():
    """
    ndarray applies formatting to given input by default
    :return:
    """
    a = np.array([1, 2, 3])
    b = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"The type of a is : {type(a)}, and value is {a}")
    print(f"The type of b is {type(b)}, and value is {b}")
    print(np.array(list(x for x in range(2, 21, 2))))

def demo_ndarray_inbuilt_formatting():
    """
    ndarray = n-dimensional array, for any given array input numpy ndarray applies formatting to align numbers
    :return: None
    """
    a_2_by_5_array_of_even_and_odd = np.array([[x for x in range(2, 11, 2)], [x for x in range(1, 10, 2)]])
    print(a_2_by_5_array_of_even_and_odd)

def demo_finding_datatypes():
    """
    numpy ndarray does not show trailing zeroes in floating point numbers
    Under the hood, numpy is implemented in C programming language for performance reasons. Its data structures
    return 64-bit numbers when we query for datatypes
    :return: None
    """
    a_floating_point_array = np.array([0.0, 0.1, 0.2, 0.3])
    print(f"The type of a floating point array is: {a_floating_point_array.dtype}, and value is {a_floating_point_array}")

    an_integer_array = np.array([1, 2, 3])
    print(f"The type of an_integer_array is {an_integer_array.dtype}, and value is {an_integer_array}")

def demo_flatten_two_dimensional_arrays():
    """
    numpy has two options to flatten 2d array - flatten() and arr.flat. The flatten() returns a copy of flattened
    array, whereas `.flat` returns a flatiter object which is a "flat-iterator" class that belongs to numpy.
    :return: None
    """
    a_2d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"The 2d array has dimensions: {a_2d_array.ndim} and shape is {a_2d_array.shape}")
    a_1d_array = a_2d_array.flatten(order='C')
    print(f"The 1d array has dimensions: {a_1d_array.ndim} and shape is {a_1d_array.shape}, and value is {a_1d_array}")

    transformed_flat = []
    for element in a_2d_array.flat:
        transformed_flat.append(element.item()**2)
    print(f"The transformed array after running through flat-iter : {transformed_flat}")

def demo_finding_array_attributes():
    """
    1. Dimensions: Depending on how array is organized, it can be 1, 2 or n-dimensional array. A matrix of 2 x 3 will be 2-dimensional array
    2. Shape: Number of rows and columns in a two-dimensional array
    :return: None
    """
    a_two_dimensional_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(f"An example of two-dimensional array, has dimensions: {a_two_dimensional_array.ndim}, with shape as {a_two_dimensional_array.shape}")

    print("------- print sizes of two dimensional array -------")
    """
    ItemSize is interesting, it is determined by the underlying compiler - Previously dtype retuned int64 which is an 8 bit integer, hence itemsize returns 8.
    """
    print(f"The size of two dimensional array is {a_two_dimensional_array.size} and item size is {a_two_dimensional_array.itemsize}")

def demo_filling_arrays_with_specific_values():
    """
    1. Create an array of zeroes, use function `zeroes`, returns floating point by default unless dtype is specified
    2. Create an array of ones, use function ones, specify dtype for int or float
    3. create a 2-dimensional array by specifying a tuple
    4. create an array full of a specific constant, specify constant while declaring the array
    :return:
    """
    array_of_zeroes = np.zeros(6, dtype=int)
    print(f"An Array of zeroes, type int : {array_of_zeroes}")

    array_of_ones = np.ones(6, dtype=float)
    print(f"An array of ones, type float: {array_of_ones}")

    an_array_of_stars = np.full((2, 3), '*')
    print(f"An array of stars: {an_array_of_stars}")


def demo_create_arrays_from_ranges():
    my_arr = np.arange(7, 2, -1, dtype=int)
    print(my_arr)

    # create floating point integers using linspace function
    my_floating_point_arr = np.linspace(0.0, 2.0, num=20)
    print(f"An array of floating points: {my_floating_point_arr}")

    reshaped_arr = np.arange(1, 100, dtype=int).reshape(9, 11)
    print(f"An array of reshaped array: {reshaped_arr}")

    print(np.arange(2, 41, 2, dtype=int).reshape(4, 5))

def broadcasting_with_arange():
    array_of_nums = np.arange(1, 5, dtype=int)
    print(f"squaring of nums: {array_of_nums ** 2}")
    print(f" cubing nums: {array_of_nums ** 3}")

if __name__ == '__main__':
    demo_ndarray_101()
    demo_ndarray_inbuilt_formatting()
    demo_finding_datatypes()
    demo_finding_array_attributes()
    demo_flatten_two_dimensional_arrays()
    demo_filling_arrays_with_specific_values()
    demo_create_arrays_from_ranges()
    broadcasting_with_arange()