from statistics import mean, median, mode


class BasicDataScienceFunctions:
    """
    All basic datascience functions or statistical functions are effectively "reduce" functions because they
    accept an iterable as input and return ONE result.
    """

    @staticmethod
    def find_min(nums: list) -> float:
        return min(nums)

    @staticmethod
    def find_max(nums: list) -> float:
        return max(nums)

    @staticmethod
    def find_sum(nums: list) -> float:
        return sum(nums)

    @staticmethod
    def find_mean(nums: list) -> float:
        return mean(nums)

    @staticmethod
    def find_median(nums: list) -> float:
        return median(nums)

    @staticmethod
    def find_mode(nums: list) -> float:
        return mode(nums)

def demo_basic_ds_functions():
    nums = [x for x in range(1, 100)]
    print(f"Find Minimum: {BasicDataScienceFunctions.find_min(nums)}")
    print(f"Find Maximum: {BasicDataScienceFunctions.find_max(nums)}")
    print(f"Find Mean: {BasicDataScienceFunctions.find_mean(nums)}")
    print(f"Find Median: {BasicDataScienceFunctions.find_median(nums)}")
    print(f"Find Mode: {BasicDataScienceFunctions.find_mode(nums)}")



if __name__ == '__main__':
    demo_basic_ds_functions()