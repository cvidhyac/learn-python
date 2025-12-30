import csv
import pandas as pd
import numpy as np


def csv_with_pandas_read_and_write():

    grades_df = pd.read_csv('../attachments/grades.csv', names=['ID', 'Name', 'Grade'])
    print(grades_df)
    contacts = np.array([[100, "Alex", "Canada"], [200, "Bob", "USA"], [300, "Charlie", "China"]])
    print(contacts)
    contacts_df = pd.DataFrame(contacts, columns=['ID', 'Name', 'Country'])
    print(contacts_df)
    contacts_df.to_csv('../attachments/emp_countries.csv', index=False)
    print("File write successful!")

def practice_csv_basics():
    try:
        with open("../attachments/grades.csv", mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([1, 'Red', "A"])
            writer.writerow([2, 'Green', "B"])
            writer.writerow([3, 'White', "A"])
        with open("../attachments/grades.csv", mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            print(f"{"ID":<10}{"Name":<10}{"Grade":>10}")
            for row in reader:
                student_id, name, grade = row
                print(f"{student_id:<10}{name:<10}{grade:>10}")

    except IOError:
        raise "Unable to write or read file in practice_csv function"


def csv_basics():
    write_csv()
    read_csv()

def read_csv():
    """
    csv reader is used for reading a csv file from disk, if file doesn't exist it will throw error
    :return:
    """
    try:
        with open('../attachments/csv_practice.csv', mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            print(f"{"ID":<10}{"NAME":<10}{"BALANCE":>10}")
            for line in reader:
                emp_id, name, balance = line
                print(f"{emp_id:<10}{name:<10}{balance:>10}")
    except IOError:
        raise "Unable to read file in read_csv function"

def write_csv():
    """
    csv writer is used for writing to file, the module documentation specifies newline should be indicated
    Also handle exceptions
    :return:
    """
    try:
        with open('../attachments/csv_practice.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([100, 'Alex', 30.45])
            writer.writerow([200, 'Bob', 90.86])
            writer.writerow([300, 'Carol', -44.56])
            writer.writerow([400, 'David', 76.23])
            writer.writerow([500, 'Emma', 67.23])
    except IOError:
        raise "Unable to write to file in write_csv function"

if __name__ == '__main__':
    csv_basics()
    print("*"*15 + "practice self check csv basics" + "*"*15)
    practice_csv_basics()
    print("*"*15 + "practice csv with pandas" + "*"*15)
    csv_with_pandas_read_and_write()