import json
from pathlib import Path


class StoringDataToFile:
    """How to use json module to store and read data and pass this between functions or modules """

    def __init__(self, num:str, input_path:str):
        self.num_to_store = int(num)
        self.as_path = Path(input_path)


    def store_to_file(self):
        as_string = json.dumps(self.num_to_store)
        self.as_path.write_text(as_string, encoding='utf-8')


class ReadingStoredData:
    """Reading stored data from a file and return using json module """

    def __init__(self, from_path:str):
        self.as_path = Path(from_path)

    def read_from_file(self) -> str:
        as_text = self.as_path.read_text()
        to_ds = json.loads(as_text)
        return to_ds


class User:
    def __init__(self, first_name:str, last_name:str, age:int):
        self.user_details = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        }

class StoreUserDetails:

    def __init__(self, user:User, as_string_path:str):
        self.user = user
        self.as_path = Path(as_string_path)

    def store_user_details(self):
        user_details_to_str = json.dumps(self.user.user_details)
        self.as_path.write_text(user_details_to_str)


def exec_favorite_nums():
    file_store = "./text_files/store_to_file.txt"
    prompt_or_quit = input("Favorite numbers, enter q to quit prompt: ")
    while prompt_or_quit != 'q':
        favorite_num = input("Enter your favorite number as numeric: ")
        if favorite_num.isnumeric():
            sdf_obj = StoringDataToFile(favorite_num, file_store)
            sdf_obj.store_to_file()
            print("Storing data success, try to store another one!")
        else:
            print("Invalid, enter only numbers")
        prompt_or_quit = input("Do you want to continue, enter q to quit: ")
        if prompt_or_quit == 'q':
            break

    print("Guessing the favorite number")
    sdf_obj_two = ReadingStoredData(file_store)
    contents = sdf_obj_two.read_from_file()
    print(f"your favorite number is {contents}!")

def exec_write_user_details():

    is_user_valid = False
    print("Store user details")

    while not is_user_valid:

        if is_user_valid:
            break

        first_name = input("Enter first_name: ")
        last_name = input("Enter last_name: ")
        age = input("Enter age: ")
        if age.isnumeric():
            user = User(first_name, last_name, int(age))
            store_details_obj = StoreUserDetails(user, "./text_files/remember-me.txt")
            store_details_obj.store_user_details()
            print("User details stored successfully!")
            is_user_valid = True
        else:
            print("Invalid user details provided, age should be a number, please try again!")

class ReadUserDetails:

    def __init__(self, path_str:str):
        self.as_path = Path(path_str)

    def read_user_details(self, ) -> dict:
        contents = self.as_path.read_text()
        return json.loads(contents)

def exec_read_user_details():
    read_user_details_obj = ReadUserDetails("./text_files/remember-me.txt")
    retrieved_user = read_user_details_obj.read_user_details()
    retrieved_user_first_name = retrieved_user["first_name"]
    print(f"User details: {retrieved_user_first_name}")



if __name__ == "__main__":
    #exec_favorite_nums()
    exec_write_user_details()
    exec_read_user_details()