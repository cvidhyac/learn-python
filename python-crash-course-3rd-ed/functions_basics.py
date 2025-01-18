from pizza_functions.make import make_pizza as mp
from pizza_functions import cook as c
from pizza_functions import deliver as d

def pass_args_in_the_order(first_name, last_name, age):
    print(f"Hello {first_name} {last_name}, your age is {age}")

def with_optional_args(product_name, price, qty=1):
    print(f"User purchased {product_name} that costs {price}, with quantity {qty}")

def passing_arbitrary_number_of_args(username, *toppings):
    print(f"Hello {username}, your pizza has total {len(toppings)} toppings! received : {toppings}")

if __name__ == "__main__":

    # pass args in order
    pass_args_in_the_order("john", "doe", 20)

    # pass args by positional
    pass_args_in_the_order(age=25, last_name="jordan", first_name="michael")

    # pass a dictionary of args as kwargs (key word args)
    dict_of_args = {
        "first_name": "john",
        "last_name": "doe",
        "age": 30
    }
    pass_args_in_the_order(**dict_of_args)

    with_optional_args("laptop", "$1200")
    with_optional_args("phone", "$700", 5)

    passing_arbitrary_number_of_args("john", "pineapple", "onion", "tomato")
    passing_arbitrary_number_of_args("mary", "cheese", "jalapeno", "pepperoni", "mushroom")

    bake_a_pizza = {
        "size": "large",
        "name": "veggie delight",
        "delivery": "today"
    }
    mp(pizza_name=bake_a_pizza["name"], size=bake_a_pizza["size"], delivery_time=bake_a_pizza["delivery"])
    c.cook_pizza(bake_a_pizza["name"], length_of_time=15, oven_type="convection")
    d.deliver_pizza("john", 23)