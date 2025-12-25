import random

import pandas as pd
import numpy as np

def transform_series_to_upper():
    series = pd.Series(np.array(["Hammer", "Wrench", "Saw", "Plier"]))
    upper_series = series.str.upper()
    print(f"Value of another_series: {upper_series}, as compared to: {series}")

def create_series_with_custom_indices():
    series = pd.Series(range(3), index=['a', 'b', 'c', 'd'])
    print(series)

def print_stats():
    an_array = pd.Series(an_integer_array())
    print(f"Mean: {an_array.mean()}")
    print(f"Minimum: {an_array.min()}")
    print(f"Maximum: {an_array.max()}")
    print(f"Sum: {an_array.sum()}")
    print(f"Count: {an_array.count()}")
    print(f"Standard Deviation: {an_array.std()}")
    print(f"Variance: {an_array.var()}")

def describe_series() -> None:
    """
    Instead of using individual methods, describe offers convenience to peek into basic stats of ndarray
    :return:
    """
    as_a_series = pd.Series(range(10))
    print(as_a_series.describe())


def create_a_series_with_index():
    with_index = pd.Series(an_integer_array(), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    print(with_index)

def create_a_series():

    as_a_series = pd.Series(an_integer_array())
    print(as_a_series)

def an_integer_array() -> np.ndarray:
    return np.arange(10, 20)

if __name__ == '__main__':
    create_a_series()
    create_a_series_with_index()
    describe_series()
    print_stats()
    transform_series_to_upper()