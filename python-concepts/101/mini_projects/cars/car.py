###
# Class naming conventions:
# 1. class name should be in camel case
# 2. There should be a docstring(""") following class definition that mentions what the class should do
# 3. Every class should have a constructor with class attributes (or __init__ ).
# Create a car and print its descriptive name
###

def create_car(name, make, year):
    return Car(name, make, year)

class Car:
    """Instantiate a car with a name and make"""
    def __init__(self, name:str, make:str, year:int, gas_tank_capacity:int=None, is_gas_tank_full:bool=False):
        self.name = name
        self.make = make
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_capacity = gas_tank_capacity
        self.is_gas_tank_full = is_gas_tank_full

    def default_gas_tank_attributes(self):
        self.gas_tank_capacity = 200
        self.is_gas_tank_full = True

    def increment_odometer_reading(self, increment_value:int):
        self.odometer_reading += increment_value

    def set_odometer_reading(self, reading:int):
        self.odometer_reading = reading

    def print_car_details(self):
        message = {
            "name_of_the_car": self.name,
            "make": self.make,
            "year_of_manufacturing": self.year,
            "odometer_reading": self.odometer_reading
        }
        print(f"car details: {message}")

    def print_descriptive_name(self):
        print(f"The {self.name} car is of type {self.make}")