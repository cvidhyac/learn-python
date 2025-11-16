class Restaurant:
    """
    Define a Restaurant class that accepts a name and cuisine, it has methods to print customers
    served and restaurant details
    """

    def __init__(self, name: str, cuisine: str):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def set_number_served(self, num_to_update: int):
        self.number_served = num_to_update

    def increment_number_served(self, value: int):
        self.number_served += value

    def print_restaurant_details(self):
        restaurant_details = {
            "name": self.name,
            "cuisine": self.cuisine,
            "Total number of people served today": self.number_served
        }
        print(f"Restaurant stats for today is: {restaurant_details}")


class User:
    """
    Create a User class that accepts first_name, last_name, has methods to greet user and print login attempts
    """
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        message = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "total_login_attempts": self.login_attempts
        }
        print(f"User information {message}")

    def greet_user(self):
        print(f"Hello {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


def exec_restaurant_operations():
    restaurant = Restaurant("Saffron", "European")
    restaurant.set_number_served(100)
    restaurant.increment_number_served(10)
    restaurant.print_restaurant_details()


def exec_user_login():
    user = User("John", "Doe")
    user.describe_user()
    for num in range(0, 4):
        user.increment_login_attempts()
        num += 1
    print("After login attempts")
    user.describe_user()
    user.reset_login_attempts()
    print("After login reset attempts")
    user.describe_user()


if __name__ == "__main__":
    exec_restaurant_operations()
    exec_user_login()
