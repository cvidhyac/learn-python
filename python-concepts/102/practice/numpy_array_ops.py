"""
Indexing and slicing
numpy accepts a subscript operator [] during indexing and slicing operations over a multi-dimensional array.
"""
import numpy as np


def select_specific_rows(an_array: np.ndarray, row_list: list):
    print(an_array[row_list])


def select_specific_columns(an_array: np.ndarray, columns: list):
    print(an_array[:, columns])


def find_row_one_column_two_value(an_array: np.ndarray, row_number: int, column_number: int):
    print(an_array[row_number, column_number])


def slicing_an_array_by_row_position(a_array: np.ndarray):
    print(a_array[0:2])


def final_practice_exercise():
    an_array = np.arange(1, 16).reshape(3, 5)
    print(an_array)
    print(f"The Second row: {an_array[1]}")
    print(f"The first and third row: {an_array[[0, 2]]}")
    print(f"Middle and three columns: {an_array[:, 1:4]}")

def demo_transpose(ndarray: np.ndarray):
    print(f"Transposed Array: {ndarray.transpose()}")

def horizontal_vertical_stacking_of_arrays():
    grades_of_class_one = np.arange(50, 60, dtype=int)
    grades_of_class_two = np.arange(60, 70, dtype=int)
    grades_of_class_three = np.arange(70, 80, dtype=int)
    print(f"Grades of class one: {grades_of_class_one}")
    print(f"Grades of class two: {grades_of_class_two}")
    print(f"Grades of class three: {grades_of_class_three}")

    print(f"After horizontal stacking: {np.hstack((grades_of_class_one, grades_of_class_two, grades_of_class_three))}")
    print(f"After vertical stacking: {np.vstack((grades_of_class_one, grades_of_class_two, grades_of_class_three))}")


    print("*"*25)

    another_array = np.arange(1, 7).reshape(2, 3)
    print(another_array)
    final_array_vstack = np.vstack((another_array, another_array)) # an array can be stacked with itself
    final_copied_array = np.hstack((final_array_vstack, final_array_vstack))
    print(final_copied_array)


if __name__ == '__main__':
    a_ndarray = np.array(
        [[x for x in np.arange(10)], [x for x in np.arange(20, 30)], [x for x in np.random.randint(40, 70, size=10)]])
    print(a_ndarray)
    select_specific_columns(a_ndarray, [0, 3, 4])
    select_specific_rows(a_ndarray, [0, 1])
    find_row_one_column_two_value(a_ndarray, 1, 2)
    final_practice_exercise()
    demo_transpose(a_ndarray)
    horizontal_vertical_stacking_of_arrays()

