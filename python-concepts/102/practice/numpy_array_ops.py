"""
Indexing and slicing
numpy accepts a subscript operator [] during indexing and slicing operations over a multi-dimensional array.
"""
import numpy as np

def select_specific_rows(an_array:np.ndarray, row_list:list):
    print(an_array[row_list])


def select_specific_columns(an_array:np.ndarray, columns:list):
    print(an_array[:, columns])

def find_row_one_column_two_value(an_array:np.ndarray, row_number: int, column_number:int):
    print(an_array[row_number, column_number])

def slicing_an_array_by_row_position(a_array:np.ndarray):
    print(a_array[0:2])


def final_practice_exercise():
    an_array = np.arange(1, 16).reshape(3, 5)
    print(an_array)
    print(f"The Second row: {an_array[1]}")
    print(f"The first and third row: {an_array[[0, 2]]}")
    print(f"Middle and three columns: {an_array[:, 1:4]}")

if __name__ == '__main__':
    a_ndarray = np.array([[x for x in np.arange(10)],[x for x in np.arange(20, 30)], [x for x in np.random.randint(40, 70, size=10)]])
    print(a_ndarray)
    select_specific_columns(a_ndarray, [0, 3, 4])
    select_specific_rows(a_ndarray, [0, 1])
    find_row_one_column_two_value(a_ndarray, 1, 2)
    final_practice_exercise()