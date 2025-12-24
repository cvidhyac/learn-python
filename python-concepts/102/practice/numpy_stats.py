"""
numpy has built-in functions for mean, median, mode, sum, range and count that operates over multidimensional arrays
saving lot of iteration code.
"""
import numpy as np


def numpy_stats():
    array = np.arange(100).reshape((10, 10))
    print(array)

    print(f"Mean: {np.mean(array)}")
    print(f"Median: {np.median(array)}")
    print(f"sum: {np.sum(array)}")
    print(f"Range: {np.max(array)}")
    print(f"Count: {np.count_nonzero(array)}")
    print(f"min: {np.min(array)}")
    print(f"variance: {np.var(array)}")
    print(f"std: {np.std(array)}")

def numpy_stats_by_row_or_columns():
    rand_arr = np.random.randint(60, 101, 12).reshape((3, 4))
    print(rand_arr)
    print(f"Average of all grades: {np.average(rand_arr)}")
    print(f"Average by rows: {np.average(rand_arr, axis=0)}")
    print(f"Average by columns: {np.average(rand_arr, axis=1)}")

if __name__ == '__main__':
    numpy_stats()
    numpy_stats_by_row_or_columns()