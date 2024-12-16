def add_ordinal(num):
    if 10 <= num % 100 <= 20:
        return "th"
    elif num % 10 == 0:
        return "th"
    elif num % 10 == 1:
        return "st"
    elif num % 10 == 2:
        return "nd"
    elif num % 10 == 3:
        return "rd"
    else:
        return "th"


def print_ordinal(list_of_nums: list):
    for num in list_of_nums:
        print(f"{num}{add_ordinal(num)}")


if __name__ == '__main__':
    print_ordinal([n for n in range(0, 10001)])
