"""
The goal of this program is to find if a given number occurs more than twice in given array
"""

"""
Option 1: Sort then compare n and n+1 is same. If not return False
with this option, the time complexity is O(n log n)
"""
def find_duplicates_twice(arr, num) -> (bool):
    sorted_arr = sorted(arr)
    array_len = len(sorted_arr) - 1
    exists = num in arr
    if not exists:
        return False

    for i in range(0, array_len):
        first_occurrence = sorted_arr[i]
        second_occurrence = sorted_arr[i + 1]
        if num == first_occurrence & num == second_occurrence:
            return True

    return False

def print_response(result, num, arr):
    if result:
        print(f"The given number {num} is present twice in array {arr}")
    else:
        print(f"The given {num} is not present in array {arr}")

def test_option_one_nlogn_complexity() -> None:
    input_arr = [1, 3, 5, 6, 7, 6, 5, 3]
    num_to_find = 8
    found = find_duplicates_twice(input_arr, num_to_find)
    print_response(found, num_to_find, input_arr)


"""

"""

if __name__ == '__main__':
    test_option_one_nlogn_complexity()