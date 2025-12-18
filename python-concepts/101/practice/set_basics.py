"""
Set is a hashable data structure, unordered and does not allow duplicates
"""


def explain_set() -> None:
    set_one = {1, 3, 4, 2, 3, 4}
    print(f"Observe the duplicates declared in input {set_one} is removed")


"""
1. Add element to set - use .add()
2. Get an element from set - similar to accessing arrays
3. Update an element - Similar to list, set is a mutable data structure
4. Remove an element - 2 ways - remove vs discard.

remove vs discard - work differently when element is not present in set. When exception should not be thrown, use discard.

"""


def explain_set_operations(a_set_of_nums:set) -> None:
    a_set_of_nums.add("Apple")
    print(a_set_of_nums)
    second_set = {5, 6, "Orange"}
    a_set_of_nums.update(second_set)
    print(a_set_of_nums)
    # Difference between remove and discard method in a python set - discard is quieter, remove throws exception
    a_set_of_nums.remove("Apple")
    print(f"After removing apple: {a_set_of_nums}")
    a_set_of_nums.discard("Poppy")
    print(f"After discarding an element that didn't exist without throwing exception: {a_set_of_nums}")

"""
union = everything in the two sets includes common and not common elements
intersection = only common elements
symmetric difference = everything in S1 not there in S2
"""
def venn_diagram() -> None:
    s1 = set()
    s2 = {5, 6, 7, 8, 8, 9}
    s1.update(s2)
    print(s1)
    print(f"S1 Union S2 returned everything in S1 and S2 together: {s1.union(s2)}")
    print(f"S1 Intersection S2 returned common between S1 and S2: {s1.intersection(s2)}")
    print(f"S1 symmetric difference with S2 returned: {s1.symmetric_difference(s2)}")

if __name__ == '__main__':
    explain_set()
    explain_set_operations({1, 3, 5, 7, 9, 8})
    venn_diagram()
