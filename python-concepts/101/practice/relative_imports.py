from mini_projects.tryit.try9192 import *
from mini_projects.tryit.update_car import exec_car
from mini_projects.cars.car import Car


def print_car_info():
    car = Car("Yellow", "Lamborghini", 1992)
    car.print_descriptive_name()

if __name__ == "__main__":
    print("----")
    three_restaurants()
    print("-----")
    print_car_info()
    print("-----")
    exec_car()
