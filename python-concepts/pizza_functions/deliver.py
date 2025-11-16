def deliver_pizza(username:str, price:int, address='Wall St'):
    _validate_username(username)
    print(f"Deliver the pizza to {username} at {address} and collect {price} in cash or credit")

def _validate_username(username:str):
   if not username.isalpha():
       raise "Invalid Username, can only contain strings"