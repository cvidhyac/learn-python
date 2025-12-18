from mini_projects.restaurants import restaurant as r


def three_restaurants():
    restaurant_one = r.Restaurant("Saffron", "Chinese")
    restaurant_two = r.Restaurant("Pink", "Asian")
    restaurant_three = r.Restaurant("Thai Fusion", "South Asian")

    restaurants = [restaurant_one, restaurant_two, restaurant_three]
    for restaurant in restaurants:
        restaurant.describe_restaurant()

