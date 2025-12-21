"""
An empty set is represented using set() instead of {} because the empty curly braces is already reserved for use
to present empty dictionaries. Hence, empty set can only be represented using set()
"""
def demo_set_review():
    text = f"To be or not to be that is the question"
    as_list = text.lower().split(" ")
    as_dict = {}
    for word in as_list:
        as_dict[word] = as_dict.get(word, 0) + 1
    as_sorted_dict = { word: count for word, count in sorted(as_dict.items()) }
    print(as_sorted_dict)
    print(f"Unique Keys: {as_sorted_dict.keys()}")


def demo_finding_subset():
    set_one = {1, 2, 3, 4, 5, 6}
    set_two = {2, 3, 4}
    print(f"is Set_two a subset of set_one : {set_two.issubset(set_one)}") # All elements must be contained in another, no extra elements
    print(f"Is Set_One a superset of set_two: {set_one.issuperset(set_two)}") ## All the elements must be contained in other, extra elements

    string_one = set("abc def ghi jkl mno")
    string_two = set("hi mom")
    print(f"Is string_one a super set of 'hi mom' {string_one.issuperset(string_two)}")


def demo_set_union():
    set_one = {1, 2, 3, 4, 5, 6}
    set_two = {2, 3, 4}

    # Using an operator
    print(f"Union using the | operator : {set_one | set_two}")
    print(f"Union using the union keyword: {set_one.union(set_two)}")

def demo_set_intersection():
    set_one = {1, 2, 3, 4, 5, 6}
    set_two = {2, 3, 4}
    print(f"Intersection using the & operator : {set_one & set_two}")
    print(f"Intersection using the intersection keyword: {set_one.intersection(set_two)}")

def demo_set_difference():
    set_one = {1, 2, 3, 4, 5, 6}
    set_two = {2, 3, 9}
    print(f"Difference using the - operator : {set_one - set_two}")
    print(f"Difference using the difference keyword : {set_one.difference(set_two)}")

def demo_set_symmetric_difference():
    """
    Find the elements that are different in both sets, leaves the common elements out
    :return:
    """
    set_one = {1, 2, 3, 4, 5, 6}
    set_two = {2, 3, 9}
    print(f"Symmetric difference using the caret operator : {set_one ^ set_two}")
    print(f"Symmetric difference using the symmetric difference keyword : {set_one.symmetric_difference(set_two)}")

def demo_disjoint():
    """
    Disjoint sets are two sets with no common elements
    :return:
    """
    set_one = {1, 2, 3, 4, 5, 6}
    set_two = {2, 3, 9}
    set_three = {9, 10}
    print(f"Disjoint using the disjoint keyword with matching elements : {set_one.isdisjoint(set_two)}")
    print(f"Disjoint set using disjoint keyword with no matching elements: {set_one.isdisjoint(set_three)}")


def practice_again():
    set_one = {10, 20, 30}
    set_two = {5, 10, 15, 20}

    print(f"To only fetch 30, we use difference of set_one and set_two: {set_one.difference(set_two)}")
    print(f"To print symmetric difference on both sets, we use symmetric difference of set_one: {set(sorted(set_one.symmetric_difference(set_two)))}")
    print(f"Now recollect union {set(sorted(set_one.union(set_two)))}")
    print(f"Now recollect intersection {set(sorted(set_one.intersection(set_two)))}")

if __name__ == '__main__':
    demo_set_review()
    demo_finding_subset()
    demo_set_union()
    demo_set_intersection()
    demo_set_difference()
    demo_set_symmetric_difference()
    demo_disjoint()
    practice_again()