import random





class Die:
    """
    Define a die class that uses random package to predict the outcome of a random dice roll
    """

    def __init__(self, sides:int = 6):
        self.sides = sides

    def roll_random_dice(self, number_of_times:int):
        for times in range(0, number_of_times):
            rolled_num = random.randint(1, self.sides)
            print(f"The {self.sides}-sided-dice rolled for {times} landed the number: {rolled_num}")


if __name__ == "__main__":
    print("------ rolling a six-sided dice 10 and 20 times")
    die = Die()
    die.roll_random_dice(10)
    die.roll_random_dice(20)

    print("---Rolling a 10-sided dice Ten and Twenty times ------")
    dieOne = Die(10)
    dieOne.roll_random_dice(10)
    dieOne.roll_random_dice(20)

    print("---Rolling a Twenty sided dice Ten and Twenty times ------")
    dieTwo = Die(20)
    dieTwo.roll_random_dice(10)
    dieTwo.roll_random_dice(20)
