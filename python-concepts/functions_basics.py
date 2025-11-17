import traceback

from pizza_functions.make import make_pizza as mp
from pizza_functions import cook as c
from pizza_functions import deliver as d

"""
In python few rules for functions - 

1. It can accept positional or kwargs (keyword arguments)
2. A function can pass default values in the function parameters, but default values should be passed at the end.
3. use `/` or `*` to force functional or kwargs. Everything before `/` uses positional, everything after `*` uses kwargs.
4. Function can be a mix of positional and kwargs, but in enterprise scenarios, we instead use typing.

Python is type-unsafe, so kwargs and typing is preferred over positional. Also specify return type as needed.

:rtype: str | None
"""

def example_to_force_positional(a_int_value: int = 0, a_str_value: str = "", /) -> str | None:
    print(f"Using positional args only: {a_int_value}, {a_str_value}")

def example_to_force_kwargs(* , a_int_value: int, a_str_value: str = "") -> str | None:
    print(f"Using keyword args only: {a_int_value}, {a_str_value}")

def example_to_understand_type_errors_in_functions():

    try:
        example_to_force_positional(a_int_value=10)
    except TypeError:
        print(f"passing kwargs in positional only function throws TypeError: {traceback.print_exc()}")

    try:
        example_to_force_kwargs("hello")
    except TypeError:
        print(f"passing only positional args without keywords throws TypeError: {traceback.print_exc()}")


def example_to_demo_positional_kwargs() -> None:
    # pass args in order
    _use_dict_to_create_kwargs("john", "doe", 20)

    # pass args by positional
    _use_dict_to_create_kwargs(age=25, last_name="jordan", first_name="michael")

    # pass a dictionary of args as kwargs (key word args)
    dict_of_args = {
        "first_name": "john",
        "last_name": "doe",
        "age": 30
    }
    _use_dict_to_create_kwargs(**dict_of_args)

def example_to_demo_optional_values():
    _with_optional_args("laptop", "$1200")
    _with_optional_args("phone", "$700", 5)

    _passing_arbitrary_number_of_args("john", "pineapple", "onion", "tomato")
    _passing_arbitrary_number_of_args("mary", "cheese", "jalapeno", "pepperoni", "mushroom")

def _use_dict_to_create_kwargs(first_name: str, last_name: str, age: int) -> None:
    print(f"Hello {first_name} {last_name}, your age is {age}")

def _with_optional_args(product_name, price, qty=1) -> None:
    print(f"User purchased {product_name} that costs {price}, with quantity {qty}")


def _passing_arbitrary_number_of_args(username, *toppings) -> None:
    print(f"Hello {username}, your pizza has total {len(toppings)} toppings! received : {toppings}")

"""
When functions are imported the module_name can be aliased similar to how we alias tables in sql
"""
def example_module_aliasing():
    bake_a_pizza = {
        "size": "large",
        "name": "veggie delight",
        "delivery": "today"
    }
    mp(pizza_name=bake_a_pizza["name"], size=bake_a_pizza["size"], delivery_time=bake_a_pizza["delivery"])
    c.cook_pizza(bake_a_pizza["name"], length_of_time=15, oven_type="convection")
    d.deliver_pizza("john", 23)


if __name__ == "__main__":
    example_to_demo_positional_kwargs()
    example_to_demo_optional_values()
    example_module_aliasing()
    example_to_understand_type_errors_in_functions()
