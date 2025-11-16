from cars.car import create_car, Car


def update_car_details(obj: Car, reading: int):
    obj.set_odometer_reading(reading)
    obj.increment_odometer_reading(200)
    print("Odometer Reading is set and incremented")

def exec_car():
    car = create_car("Black", "Fiat", 2012)
    update_car_details(car, 122)
    car.print_car_details()