from car import Car

class NormalCar(Car):

    def __init__(self, name:str, make:str, year:int, odometer_reading:int = 100):
        super().__init__(name, make, year)
        self.odometer_reading = odometer_reading
        self.gas_tank_capacity = 100
        self.is_gas_tank_full = False

    def print_car_details(self):
        print("Printing details for normal car")
        super().print_car_details()

    def print_descriptive_name(self):
        print("Describing normal car")
        super().print_descriptive_name()

class ElectricCar(Car):
    """Subclass that contains method to create electric car"""

    def __init__(self, name, make, year, odometer_reading:int = 500):
        super().__init__(name, make, year)
        self.odometer_reading = odometer_reading
        self.battery_operated = True
        self.gas_tank_capacity = 0
        self.battery_charge_percent = 76

    def describe_electric_car(self):
        print(f"The electric car {self.name} is made by {self.make} and is currently charged at {self.battery_charge_percent}")


if __name__ == "__main__":
    normal_car = NormalCar("Sedan", "Toyota", 2006)
    electric_car = ElectricCar("SUV", "Tesla", 2023, 10000)

    normal_car.print_car_details()
    electric_car.print_car_details()
    electric_car.describe_electric_car()