###
# Create a car and print its descriptive name
###
class Car:
    """Instantiate a car with a name and make"""
    def __init__(self, name:str, make:str):
        self.name = name
        self.make = make

    def print_descriptive_name(self):
        print(f"The {self.name} car is of type {self.make}")