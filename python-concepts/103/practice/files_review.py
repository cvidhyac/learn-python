import os


def create_new_file() -> None:
    """
    with helps in resource management by autoclosing the resource upon exit
    mode=w is for writing mode
    :return:
    """
    with open('/tmp/temp.txt', mode='w') as tempFile:
        tempFile.write("Hello World!!\n")
        tempFile.write("Learning Python!\n")
        tempFile.write(str(os.getpid()))

    os.rename('/tmp/temp.txt', '/tmp/temp_with_pid.txt')
    temp_pid_file = open('/tmp/temp_with_pid.txt', mode='r')
    with temp_pid_file:
        for line in temp_pid_file:
            print(line)
    os.remove('/tmp/temp_with_pid.txt')


def demo_update_file_contents() -> None:
    """
    os.rename can help rename as well as move files
    os.remove helps remove a file from disk
    :return:
    """
    temp_file = open('../attachments/temp.txt', mode='w')
    orig_file = open('../attachments/accounts.txt', mode='r')
    with temp_file, orig_file :
        for line in orig_file:
            emp_id, name, salary = line.split(" ")
            if name.casefold() != "rose":
                temp_file.write(line)
            else:
                name = "Joseph"
                new_line = emp_id + " " + name + " " + salary
                temp_file.write(new_line)

    os.rename('../attachments/temp.txt', '../attachments/accounts.txt')
    print("Done updating file contents")

def read_file_with_formatting():
    """
    mode=r helps to read a file, f strings can be formatted for fixed width for better readability
    :return:
    """
    with open('../attachments/accounts.txt', mode='r') as read_file:
        headline = f"{"Account_ID":<15}{"Name":<10}{"Balance": <10}"
        print(headline)
        for line in read_file:
            account_id, name, balance = line.split()
            print(f"{account_id:<15}{name:<10}{float(balance):.3f}")

def read_all_lines_from_file() -> None:
    """
    `file_obj.readlines()` help read all lines from a file, however it is very memory intensive for large files
    The iterator way of reading is more memory efficient because it only reads one line at a time.
    :return: None
    """
    with open('../attachments/accounts.txt', mode='r') as read_file:
        all_lines = read_file.readlines()
        for line in all_lines:
            print(line.replace("\n", "")) #print already has `\n separator

if __name__ == '__main__':
    print("*"*15 + "create_new_file" + "*"*15)
    create_new_file()
    print("*"*15 + "update_file_contents" + "*"*15)
    demo_update_file_contents()
    print("*"*15 + "read_file_with_formatting" + "*"*15)
    read_file_with_formatting()
    print("*"*15 + "read_all_lines_from_file" + "*"*15)
    read_all_lines_from_file()