## Practice file in read, write, append modes
## Shelve module -  save data in raw format

import shelve


def open_file_as_read(file_path):
  file = open(file_path, "r")
  contents = file.readlines()
  for line in contents:
    print(line)


def file_append(file_path):
  last_line_content = "last line"
  file = open(file_path, "a")
  file.write("\n")
  file.write(last_line_content)
  file.close()


def print_last_line_in_a_file(file_path):
  last_line_content = "last line"
  read_file = open(file_path, "r")
  lines = read_file.read().splitlines()
  last_line = lines[-1]
  assert last_line_content == last_line


def shelve_demo(file_path):
  read_file = open(file_path, "r")
  read_contents_as_list = read_file.read().splitlines()

  # Create a shelve file with open function and write a list to it
  write_dat_file = shelve.open("resources/new_data_file")
  write_dat_file['file_contents'] = read_contents_as_list
  write_dat_file.close()
  # Read the lsit and continue processing
  shelve_file = shelve.open("resources/new_data_file")
  print("The length of shelve_read list is : " + str(
      len(shelve_file['file_contents'])))


def demo():
  file_path = "resources/email_phone_numbers.txt"
  open_file_as_read(file_path)
  file_append(file_path)
  print_last_line_in_a_file(file_path)
  shelve_demo(file_path)


demo()
