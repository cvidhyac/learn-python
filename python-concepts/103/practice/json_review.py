import json

def write_json_to_file():
    """
    json.dump writes the given json object structure / dictionary to a file
    :return:
    """
    accounts_json = {
        "accounts": [
            {"account_id": 1, "name": "Jones", "balance": 1000},
            {"account_id": 2, "name": "Smith", "balance": 2000},
            {"account_id": 3, "name": "Jason", "balance": 3000},
        ]
    }
    with open('../attachments/accounts.json', 'w') as file:
        json.dump(accounts_json, file, indent=4)

def convert_as_string():
    """
    dumps = dump as string
    json.dumps() returns a string, very useful for conversion operations
    :return:
    """
    accounts_json = {
        "accounts": [
            {"account_id": 1, "name": "Jones", "balance": 1000},
            {"account_id": 2, "name": "Smith", "balance": 2000},
            {"account_id": 3, "name": "Jason", "balance": 3000},
        ]
    }
    to_string_value = json.dumps(accounts_json)
    print(to_string_value)

def read_json_object_from_memory():
    accounts_json = {
        "accounts": [
            {"account_id": 1, "name": "Jones", "balance": 1000},
            {"account_id": 2, "name": "Smith", "balance": 2000},
            {"account_id": 3, "name": "Jason", "balance": 3000},
        ]
    }
    print(accounts_json["accounts"][0])

def read_json_as_file():
    """
    json.load method helps read a file containing json objects.
    :return:
    """
    with open('../attachments/accounts.json', 'r') as read_file:
        accounts_json = json.dumps(json.load(read_file), indent=4)
        print(accounts_json)

if __name__ == '__main__':
    write_json_to_file()
    print("*"*15 + "convert_as_string" + "*"*15)
    convert_as_string()
    print("*"*15 + "read-json-object-from-memory" + "*"*15)
    read_json_object_from_memory()
    print("*"*15 + "read_json_as_file" + "*"*15)
    read_json_as_file()
