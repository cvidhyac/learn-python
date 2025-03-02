def print_person_details(first_name: str, last_name: str, age: int, city: str):
    person = {"first_name": first_name, "last_name": last_name, "age": age, "city": city}
    print(f"Person details {person}")


def print_person_details_as_kwargs(**kwargs):
    print(f"Attributes are {kwargs['first_name']} {kwargs['last_name']} {kwargs['age']}")

def print_favorite_numbers():
    person_and_lucky_numbers = {"John": 5, "Jane": 10}
    for person_name, lucky_number in person_and_lucky_numbers.items():
        print(f"Lucky number of {person_name} is {lucky_number}")


def sorting_a_dictionary():
    person_and_age = {"Mary": 23, "Joe": 35, "Albert": 56, "Diana": 97, "George": 15}
    for person in sorted(person_and_age.keys()):
        print(f"Sorted Alphabetically, person is : {person}")

def dictionary_as_kwargs() :
    person = {
        "first_name": "john",
        "last_name": "doe",
        "age": 20
    }
    return person


def polling_favorite_languages(person: str):
    devs_and_programming = {
        "Abe": "Pascal",
        "Bob": "Cobol",
        "Charlie": "Java",
        "Adam": "Java",
        "Mary": "Python",
        "Dobby": "Java",
        "Fiona": "Python",
        "Gabe": "Rust",
        "Harry": "C",
        "Issac": "Java",
        "Kyle": "Python",
        "Larry": "C",
        "Maggie": "Java",
        "Nathan": "Rust"
    }
    temp_dict = devs_and_programming
    print(f"dictionary size before deletion : {len(temp_dict)}")
    del temp_dict["Abe"]
    temp_dict.pop("Fiona")
    temp_dict.popitem() # Deletes the last inserted item since python 3.7, before that it used be a random element
    print(f"Dictionary size after deletion: {len(devs_and_programming)}")
    temp_dict.clear()
    print(f"Temporary dictionary is cleared, length: {len(temp_dict)}!")

    has_person_taken_the_poll = devs_and_programming.get(person, f"{person} did not take the poll yet!")
    print(has_person_taken_the_poll)
    unique_programming_languages = set(devs_and_programming.values())
    print(f"{unique_programming_languages} are the unique programming languages in this poll")
    total_language_list = tuple(devs_and_programming.values())
    for prog_lang in unique_programming_languages:
        print(f"number of people that like {prog_lang}: {total_language_list.count(prog_lang)}")

def print_favorite_places() :
    my_favorite_places = { "John": "Vienna", "Sidney": "Florida", "Albert": "Banff"}
    for person, favorite_place in my_favorite_places.items():
        print(f"Favourite place of {person} is {favorite_place}")

def print_nested_dictionary():

    my_website_users = {
        "auser": {
            "first_name": "john",
            "last_name": "doe",
            "age": 45
        },
        "dragongirl": {
            "first_name": "Amelia",
            "last_name": "Rose",
            "age": 32
        }
    }
    for user_name, user_info in my_website_users.items():
        # Using get() to retrieve an element from dictionary returns None if element is not present
        # If it was retrieved using square brackets throws KeyError if element is not present
        print(f"{user_name}'s real name is {user_info.get('first_name').title()} {user_info.get('last_name').title()}")

if __name__ == '__main__':
    print_person_details("John", "Doe", 65, "Alberta")
    print_favorite_numbers()
    sorting_a_dictionary()
    polling_favorite_languages("Ellie")
    print_favorite_places()
    print_nested_dictionary()
    print_person_details_as_kwargs(**dictionary_as_kwargs())