from cars.models import create_car, Car


def update_car_details(obj: Car, reading: int):
    obj.set_odometer_reading(reading)
    print("Reading is updated")
    obj.print_car_details()

def exec_car():
    car = create_car("Black", "Fiat", 2012)
    update_car_details(car, 122)

if __name__ == "__main__":
    exec_car()
