from copy import deepcopy
from types import MappingProxyType


def execute_an_update(*args) -> None:
    items = [*args]
    for item in items:
        print(f"Item: {item}, its type: {type(item)}")
        if type(item) == list:
            item.append(5)
        elif type(item) == str:
            item = item * 2  # observe no effect, string is immutable type
        elif type(item) == int:
            item = item * 2  # observe no effect, int is immutable type
        elif type(item) == dict:
            item.pop("keyTwo")
        elif type(item) == set:
            item.add(15)
    print(f"Inside method: {items}")


"""
Python uses the concept of "pass-by-object-reference" which is a hybrid of pass by value and pass by reference.
This is its default behaviour.

When an immutable type is passed, a copy is created (acts like pass-by-value)
When a mutable type is passed, it refers to the same container (acts like pass-by-reference)

Strategies to prevent unpredictable behaviour using mutable types:
- convert it to an immutable type before passing it to a function
- use a shallow / deep copy operation so that the behavior is predictable.

"""


def how_does_python_references_work():
    an_int, a_list, a_string, a_set, a_dict = 1, [1, 2], "Hello", {1, 3, 5}, {"keyOne": "valueOne",
                                                                              "keyTwo": "valueTwo"}

    an_int, a_second_list, a_string, a_second_set, a_second_dict = 1, [1, 2], "Hello", {1, 3, 5}, {"keyOne": "valueOne",
                                                                                                   "keyTwo": "valueTwo"}

    # MappingProxyType is a read-only view of dict, note that to make it immutable use fresh copy instead of original
    an_immutable_list, an_immutable_set, an_immutable_dict = tuple(deepcopy(a_list)), frozenset(
        deepcopy(a_set)), MappingProxyType(deepcopy(a_dict))

    print("="*50)
    execute_an_update(an_int, a_list, a_string, a_set, a_dict)
    print(f"Outside method, observe original is modified : {an_int, a_list, a_string, a_set, a_dict}")

    print("="*50)
    execute_an_update(an_int, deepcopy(a_second_list), deepcopy(a_second_set), deepcopy(a_second_dict))
    print(
        f"Outside method, print original : {a_second_list} {a_second_set} {a_second_dict}")  # a deep copied list still produces a mutable type

    print("="*50)
    execute_an_update(an_int, an_immutable_list, a_string, an_immutable_set,
                                                     an_immutable_dict)
    print(f"Outside method with true immutable types : { an_immutable_list, an_immutable_set, an_immutable_dict}")


"""
    Shallow copy = Another copy of the same id() is created, it is not a true copy of internals.
    During shallow copy any modifications made to parent object affects all copies.

    Deep copy = True copy of the object, any changes made to parent does not affect copies.
"""


def how_does_shallow_deep_copy_work() -> None:
    list_one = [1, 2, 3, 4, 5, 6]
    list_two = list_one.copy()  # shallow copy
    list_three = list_one.copy()
    print(f"List Three: {list_three}")
    list_four = deepcopy(list_one)
    print(f"Shallow copy ID's are the same: {id(list_one)} {id(list_two)}")
    list_two.insert(2, "Apple")  # type: ignore
    print(f"value of List 2: {list_two} and this is value of List 3: {list_two}")
    print(f"value of list 4: {list_four}")


if __name__ == "__main__":
    how_does_shallow_deep_copy_work()
    print("=" * 50)
    how_does_python_references_work()
