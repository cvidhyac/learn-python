import numpy as np


def ufunc_sqrt():
    an_arr = list(x**2 for x in np.arange(1, 101, dtype=int))
    print(an_arr)
    sqrt_arr = np.sqrt(an_arr)
    print(sqrt_arr)

def ufunc_add():
    an_arr = np.arange(1, 101, dtype=int)
    print(an_arr)
    another_arr = np.arange(200, 300, dtype=int)
    print(another_arr)
    print(np.add(an_arr, another_arr))
    print(np.multiply(an_arr, another_arr))

def ufunc_power():
    an_arr = np.arange(1, 6, dtype=int)
    print(f"Original array : {an_arr}")
    with_power = np.power(an_arr, 3) # cube each element in the array
    print(f"With power universal function: {with_power}")
    with_broadcasting = with_power ** 5
    print(f"With broadcasting : {with_broadcasting}")

if __name__ == '__main__':
    ufunc_sqrt()
    ufunc_add()
    ufunc_power()