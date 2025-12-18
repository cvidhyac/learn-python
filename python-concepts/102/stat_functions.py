from functools import reduce
from statistics import mean, median, mode


class BasicDataScienceFunctions:
    """
    All basic datascience functions or statistical functions are effectively "reduce" functions because they
    accept an iterable as input and return ONE result.
    """

    @staticmethod
    def find_min(a_list: list) -> float:
        return min(a_list)

    @staticmethod
    def find_minimum_case_insensitive(a_list: list) -> str:
        return min(a_list, key=lambda val: str(val).casefold())

    @staticmethod
    def find_max(a_list: list) -> float:
        return max(a_list)

    @staticmethod
    def find_sum(a_list: list) -> float:
        return sum(a_list)

    @staticmethod
    def find_mean(a_list: list) -> float:
        return mean(a_list)

    @staticmethod
    def find_median(a_list: list) -> float:
        return median(a_list)

    @staticmethod
    def find_mode(a_list: list) -> float:
        return mode(a_list)

def demo_basic_ds_functions():
    nums = [x for x in range(1, 100)]
    print(f"Find Minimum: {BasicDataScienceFunctions.find_min(nums)}")
    print(f"Find Maximum: {BasicDataScienceFunctions.find_max(nums)}")
    print(f"Find Mean: {BasicDataScienceFunctions.find_mean(nums)}")
    print(f"Find Median: {BasicDataScienceFunctions.find_median(nums)}")
    print(f"Find Mode: {BasicDataScienceFunctions.find_mode(nums)}")


def demo_with_case_insensitivity() -> None:
    foods = ['Cookies', 'pizza', 'Grapes', 'apples', 'steak', 'Bacon']

    minimum_with_case = BasicDataScienceFunctions.find_min(foods)
    print(f"Minimum With Case: {minimum_with_case}")

    minimum_value = BasicDataScienceFunctions.find_minimum_case_insensitive(foods)
    print(f"Minimum value case insensitive: {minimum_value}")


def demo_with_zip():
    """
    Produce a tuple by adding indices of elements after running a zip function.
    :return: None
    """
    list_one = [1, 2, 3]
    list_two = [4, 5, 6]
    list_three = tuple(a + b for a, b in zip(list_one, list_two))
    print(f"List Three after zip: {list_three}")

if __name__ == '__main__':
    demo_basic_ds_functions()
    demo_with_case_insensitivity()
    demo_with_zip()