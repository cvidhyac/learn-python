###
# Create a car and print its descriptive name
###

def create_car(name, make, year):
    return Car(name, make, year)

class Car:
    """Instantiate a car with a name and make"""
    def __init__(self, name:str, make:str, year:int):
        self.name = name
        self.make = make
        self.year = year
        self.odometer_reading = 0

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