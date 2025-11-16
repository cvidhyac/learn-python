"""
Shallow copy = Another copy of the same id() is created, it is not a true copy of internals.
During shallow copy any modifications made to parent object affects all copies.

Deep copy = True copy of the object, any changes made to parent does not affect copies.
"""

import copy



if __name__ == "__main__":

    list_one = [1, 2, 3, 4, 5, 6]
    list_two = list_one.copy() # shallow copy
    list_three = list_one.copy()
    list_four = copy.deepcopy(list_one)
    print(f"Shallow copy ID's are the same: {id(list_one)} {id(list_two)}")
    list_two.insert(2, "Apple")
    print(f"value of List 2: {list_two} and this is value of List 3: {list_two}")
    print(f"value of list 4: {list_four}")
