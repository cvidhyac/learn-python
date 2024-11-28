def check_seasons(user_val: str):
    seasons = ("Spring", "Summer", "Winter", "Fall", "Autumn")
    calamities = ("Hurricane", "Tsunami", "Typhoon", "Cyclone", "Earthquake")
    if user_val in seasons:
        print(f"User provided value is a season, received: {user_val}")
    elif user_val in calamities:
        print(f"{user_val} is a type of natural disaster")
    else:
        print(f"{user_val} is neither a season nor a natural disaster")


def is_admin(username: str):
    if username == "admin":
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again!")


def hello_admin(users:list[str]):
    if not users:
        print("we need to find some users!")
    else:
        for user in users:
            is_admin(user)

def check_usernames(current_users:list[str], new_users:list[str]):
    case_insensitive_current_user_list = [current_user.lower() for current_user in current_users]
    case_insensitive_new_user_list = [new_user.lower() for new_user in new_users]
    if not (new_users or current_users):
        print(f"One of new users list: {new_users} or current users list {current_users} is empty ")
    else:
        for new_user in case_insensitive_new_user_list:
            if new_user in case_insensitive_current_user_list:
                print(f"{new_user} username is already taken, choose another username")
            else:
                print(f"{new_user} username is available")

def print_ordinal_numbers():
    nums = [num for num in range(0, 10)]
    first_ordinal_prefix = "st"
    second_ordinal_prefix = "nd"
    third_ordinal_prefix = "rd"
    default_ordinal_prefix = "th"

    for num in nums:
        if num == 1:
            print(f"{num}{first_ordinal_prefix}")
        elif num == 2:
            print(f"{num}{second_ordinal_prefix}")
        elif num ==3:
            print(f"{num}{third_ordinal_prefix}")
        else:
            print(f"{num}{default_ordinal_prefix}")

if __name__ == '__main__':
    check_seasons("Pizza")
    check_seasons("Typhoon")
    check_seasons("Winter")
    a_list = ["admin", "joe", "john", "jane", "doe"]
    hello_admin(a_list)
    hello_admin([])
    check_usernames(["JOHN", "JOE", "Jelly", "Doe", "Jane"], ["jane", "joe", "harry", "george"])
    print_ordinal_numbers()