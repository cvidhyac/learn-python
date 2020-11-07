## Use shutil package for copy, move functions
## Use os.unlink for deleting files as a irreversible operation.
## Use send2Trash module for sending files to trash


import os
import shutil
import send2trash

# Use shutil.copy to copy a specific file with a new name
def file_copy():
  new_copy_name = shutil.copy("./resources/email_phone_numbers.txt",
                              "./resources/email_backup")
  print("file copied: " + new_copy_name)


# Use Copy Tree to copy an entire directory path
def directory_copy():
  new_dir_location = shutil.copytree("./resources", "./resources_backup")
  print("directory copied : " + new_dir_location)


# Same effect as a file rename
def file_move():
  new_file_path = shutil.move("./resources/email_backup",
                              "./resources/email_renamed")
  print("The new file path is : " + new_file_path)


def delete_file():
  os.unlink("./resources/email_renamed")
  print("file email_renamed is deleted, cannot be recovered")


def delete_directory():
  shutil.rmtree("./resources_backup")
  print(
    "the provided directory resources_backup is deleted, cannot be recovered")

def send_to_trash():
  shutil.copytree("./resources", "./resources_backup")
  path =  send2trash.send2trash("./resources_backup")
  print("Path sent to trash : " + "./resourcees_backup")

def demo():
  file_copy()
  directory_copy()
  file_move()
  delete_file()
  delete_directory()
  send_to_trash()

demo()
