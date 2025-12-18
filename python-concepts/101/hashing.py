"""
A data structure becomes hashable if it implements the hash function
Python has a `hash` function that converts a large data into an integer value through the hashing process.
Python has two types of data structures -  hashable and non-hashable.

Immutable data structures usually have hash in-built - tuples, str can print hash function
Set and Dictionary are hash based data structures: It means that these data structures only accept immutable types.

What is the real life use case or one key benefit of using a hashable data structure?
- In un-hashed data structures, to find an element in the list, we need one full iteration.
- Hashed data structures are able to find elements in a large data set lot faster than un-hashed data structure.
"""
def explain_hash_function():
    try:
        my_list = [1, 2, 3]
        print(hash(my_list))
    except TypeError:
        print("List is an unhashable data structure, whereas set and dict are hashable")
    my_tuple = (1, 2, 3)
    print(hash(my_tuple))
    my_string = "sefdf"
    print(hash(my_string))


if __name__ == '__main__':
    explain_hash_function()
