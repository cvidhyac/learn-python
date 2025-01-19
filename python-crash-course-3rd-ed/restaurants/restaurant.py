

class Restaurant:

    # define constructor
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name}, it serves {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print("The restaurant is open!")

