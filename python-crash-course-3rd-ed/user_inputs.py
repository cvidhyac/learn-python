def rental_car():
    print("Welcome to Avis, please find our rental car selections")
    print("Choose from one of the following")
    car_reservation = {
        1: "Honda",
        2: "Fiat",
        3: "Subaru",
        4: "Audi",
        5: "Lexus"
    }
    print(car_reservation)
    is_valid_selection = False
    while not is_valid_selection:
        car_selection = input("Enter a the number of the type of car you wish to reserve: ")
        if not car_selection.isnumeric():
            print("Invalid selection, Please retry and enter only numbers")
        elif int(car_selection) not in car_reservation.keys():
            print(f"Invalid option, Please only enter one of the numbers {tuple(car_reservation.keys())}")
        else:
            print(f"Valid selection, you entered: {car_selection}")
            print_confirm = input("Enter YES to confirm, input y/Y: ")
            if print_confirm == 'y' or print_confirm == "Y" or print_confirm.lower() == "yes":
                print("Your reservation is confirmed")
                is_valid_selection = True
            else:
                print("Your reservation is aborted, please try again later")
                break


def restaurant_seating():

    is_allowed_guests = False
    while not is_allowed_guests:
        num_of_guests = input("How many guests do you need a table for: ")
        if not num_of_guests.isnumeric():
            print("Please only enter numbers, preferably less than 8")
        elif int(num_of_guests) > 8:
            print("We do not have seats for 8 or more guests, please reduce the number")
        else:
            print("Thank you, you may now enter our waiting area")
            is_allowed_guests=True


def multiples_of_ten(num: int):
    if num % 10 == 0:
        print(f"{num} is a multiple of 10")
        return True
    else:
        print(f"{num} is not a multiple of 10")
        return False

def copy_lists_over():
    list_one = ["Jane", "Joe", "Albert"]
    list_two = []
    while list_one:
        list_two.append(list_one.pop())
    print(list_two)


def run_the_game():
    user_options = {
        1: "rental car reservation",
        2: "restaurant seating",
        3: "Move a list of people",
        4: "Fun math game"
    }
    program_to_run = input(f"Choose a number to select the program to run {user_options} : ")
    is_valid_option = False
    while not is_valid_option:
        if not program_to_run.isnumeric():
            print("Enter only numbers shown above")
        elif int(program_to_run) == 1:
            is_valid_option = True
            rental_car()
        elif int(program_to_run) == 2:
            is_valid_option = True
            restaurant_seating()
        elif int(program_to_run) == 3:
            is_valid_option = True
            copy_lists_over()
        else:
            is_valid_option = True
            guess_number = input("Enter a number to play: ")
            if guess_number.isnumeric():
                multiples_of_ten(int(guess_number))
            else:
                print("Invalid Selection: Game Over!")


def sandwich_orders(list_of_sandwiches: list[str]):
    print(f"sandwiches to be made - {sandwiches}")
    finished_sandwiches = []
    if "pastrami" in list_of_sandwiches:
        print("The deli has run out of pastrami, removing all pastrami sandwiches from the order now")
        while "pastrami" in list_of_sandwiches:
            sandwiches.remove("pastrami")
        print(f"Now starting to prepare the remaining sandwiches {sandwiches}")

    while sandwiches:
        prepared_sandwich = sandwiches.pop()
        finished_sandwiches.append(prepared_sandwich)
    for sandwich in finished_sandwiches:
        print(f"I made your {sandwich.title()} sandwich")

def no_pastrami(list_of_sandwiches: list[str]):
    list_of_sandwiches.append("pastrami")
    list_of_sandwiches.append("pastrami")
    list_of_sandwiches.append("pastrami")

    sandwich_orders(sandwiches)

if __name__ == '__main__':
    # run_the_game()
    sandwiches = ["Cheese", "grilled-cheese", "Veggie", "Green Goddess", "tomato", "Chili"]
    sandwich_orders(sandwiches[:])
    no_pastrami(sandwiches[:])

