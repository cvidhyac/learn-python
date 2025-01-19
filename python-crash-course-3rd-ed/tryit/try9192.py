from restaurants.restaurant import *

def three_restaurants():
    restaurant_one = Restaurant("Saffron", "Chinese")
    restaurant_two = Restaurant("Pink", "Asian")
    restaurant_three = Restaurant("Thai Fusion", "South Asian")

    restaurants = [restaurant_one, restaurant_two, restaurant_three]
    for restaurant in restaurants:
        restaurant.describe_restaurant()