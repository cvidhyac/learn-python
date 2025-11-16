from pathlib import Path

def read_all_contents(file_path:Path):
    lines = file_path.read_text().strip().splitlines()
    for line in lines:
        print(line.strip())

class FindBirthday:
    """Find Birthday is present in the million digits"""
    def __init__(self, file_path:Path, bday:str):
        self.file_path = file_path
        self.bday = bday

    def read_file_contents(self) -> str:
        file_contents = self.file_path.read_text(encoding='utf-8').strip()
        return file_contents

    def find_bday(self) -> bool:
        file_contents = self.read_file_contents()
        if self.bday in file_contents:
            return True
        else:
            return False


if __name__ == "__main__":
    path = Path('pi_digits.txt')
    read_all_contents(path)
    print("-------------------------------")

    prompt_or_quit = input("Birthday finder, enter 'q' to quit: ")
    while prompt_or_quit != 'q':
        bday = input("Enter your birthday in ddmmyy format to search in million digits of pi: ")
        if bday.isnumeric() or len(bday)>6:
            find_birthday_obj = FindBirthday(Path('pi_million_digits.txt'), bday)
            is_bday_present = find_birthday_obj.find_bday()
            if is_bday_present:
                print(f"Found birthday in million digits: {bday}")
                break
            else:
                print("Birthday not found, please try again!")
        else:
            print("Invalid birthday entered, it should only contain numbers")
