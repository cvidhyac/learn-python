import string

import numpy as np
from copy import deepcopy

def demo_creating_views() -> None:
    """
    A view is different from a shallow copy operation. It appears like a copy, it has two different ID,
    however any change made to the view also reflects in the parent copy and vice versa. Any change made to
    parent copy also reflects in the view EVEN if its ID is different.
    :return: None
    """
    a = np.arange(1, 10, 2)
    b = a.view()
    print(f"Before modifying view, ID of a: {id(a)} and ID of b: {id(b)}")
    b *= 10
    print(f"After modifying view, value of B: {b}, and its id: {id(b)}, value of a: {a} and its id: {id(a)}")


def demo_slicing_operation_shallow_copy() -> None:
    """
    In numpy, a slicing operation creates a shallow copy, it behaves like a view
    :return: None
    """
    a = np.arange(1, 20, 2)
    b = a[3:7]
    print(f"Initial values of a: {a}, and its id: {id(a)}, and B as a slice of a: {b}, and id of B: {id(b)}")
    b *= 10
    print(f"After modifying B, we have a: {a} and its ID: {id(a)}, and see that it matches B, value: {b}, and its id: {id(b)}")
    b = b * 20
    print(f"However if we use a object reference during transformation it loses the association, the effect is {b}, and A is not modified : {a}")


def demo_deep_copy() -> None:
    """
    numpy has a copy method which creates a deep copy
    :return: None
    """
    a = np.array([1, 2, 3])
    b = a.copy()
    print(f"Before deep copy {a}, and its id: {id(a)}")
    print(f"Assign a copy as B, value {b}, and its id: {id(b)})")
    a[2] = 5
    print(
        f"""Now B is reassigned another value, we verify A is not affected: {a}, 
        as compared to B: {b} and its id for A: {id(a)}, and ID for B: {id(b)}""")

    d = { "a_list_of_nums" : np.arange(50, 100, 2),
          "a_list_of_strings": np.random.default_rng().choice(list(string.ascii_uppercase), 10)
        }

    e = deepcopy(d)

    print(f"Value of d before deep copy {d}, and its id: {id(d)}")
    print(f"Value of e after deep copy {e}, and its id: {id(e)}")
    print(f"Now modifying E to add another element")
    e["another_list"] = np.random.default_rng().integers(low=10, high=20, size=15)
    print(f"Now check if D contains this element, {d.__contains__("another_list")}")
    print(f"Value of D after deep copy {d}, and its id: {id(d)}")
    print(f"Value of E after deep copy {e}, and its id: {id(e)}")

def demo_flatten_ravel():
    """
    Flatten and Ravel are 2 methods in numpy that help flatten a numpy ndarray to one-dimensional array
    However, there are key differences - Flatten returns a deep copy, however ravel is a view that shows the data one-dimensional internally
    modifications will affect parent
    :return:
    """
    an_array = np.arange(1, 16).reshape(3, 5)
    print(an_array)
    flattened = an_array.flatten()
    print(f"Value of flattened array: {flattened}")
    flattened[2] = 100
    print(f"After modifying one element in flattened array: {flattened} and original is not modified {an_array}")
    raveled = an_array.ravel()
    raveled[2] = 100
    print(f"After raveled array is modified : {raveled} and original is modified {an_array}")

if __name__ == '__main__':
    print("-"*15)
    demo_creating_views()
    print("-"*15)
    demo_slicing_operation_shallow_copy()
    print("-"*15)
    demo_deep_copy()
    print("-"*15)
    demo_flatten_ravel()
    print("-"*15)