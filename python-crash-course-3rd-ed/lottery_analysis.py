from random import choice
from random import sample
from string import ascii_lowercase

def lottery_prize_winner(nums:tuple, letters:tuple):

    chosen_numbers = []
    chosen_letters = []

    for num in range(0, 4):
        chosen_numbers.append(choice(nums))
        chosen_letters.append(choice(letters))

    return chosen_letters, chosen_numbers

if __name__ == "__main__":
    random_letters = [letter for letter in ascii_lowercase[:10]]
    random_population_nums = [num for num in range(20, 31)]
    random_numbers = sample(random_population_nums, k=10)
    lottery_letters, lottery_numbers = lottery_prize_winner(nums=tuple(random_numbers), letters=tuple(random_letters))
    print(f"You win a prize if your ticket has the following numbers {lottery_numbers} or letters {lottery_letters}")

