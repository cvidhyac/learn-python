def open_restaurant():
    print("The restaurant is open!")


class Restaurant:
    """
    Define a restaurant class and print if it is open or not
    """

    # define constructor
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
        """
        In python, there are no in-built access modifiers such as private or protected. The data hiding
        or encapsulation works by only exposing variables via the initializer, then access the variables
        through functions
        :return: None
        """
        print(f"The restaurant's name is {self.restaurant_name}, it serves {self.cuisine_type} cuisine")

