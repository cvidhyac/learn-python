class ExceptionBasics:
    """Demo the try-except-else example using a division calculator"""

    def __init__(self, first_num:str, second_num:str):
        self.first_num = int(first_num)
        self.second_num = int(second_num)

    def divide_two_numbers(self) -> float | None:
        try:
            result = self.first_num / self.second_num
        except ZeroDivisionError:
            print("Cannot divide by zero, try again!")
        else:
            return result


if __name__ == "__main__":
    prompt_or_quit = input("Division Calculator, enter two numbers or press 'q' to quit: ")
    while prompt_or_quit != 'q':
        first_number = input("Enter first number: ")
        second_number = input("Enter second number: ")

        if first_number.isnumeric() and second_number.isnumeric():
            exception_demo = ExceptionBasics(first_number, second_number)
            answer = exception_demo.divide_two_numbers()
            if answer is not None:
                print(f"Good choice, answer is : {answer}")
        elif first_number == 'q' or second_number == 'q':
            print("Thank you for playing, good bye!")
            break
        else:
            print("Invalid selection, try again entering only numeric")