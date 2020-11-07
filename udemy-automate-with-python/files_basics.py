# Practice basic file functions
## Use functions available in os module for getting current directory path
## Use list directory, and practicce joins, find size
## Use os.walk for listing foldernames, subdirectories, filenames within

import os


def print_current_working_directory():
    print("The current working directory is " + os.getcwd())


def print_path_functions():
    print("Current Directory is : " + os.path.curdir)
    print("Directory size is : " + str(os.path.getsize(os.path.curdir)))
    print("Is README.md a file : " +
          str(os.path.isfile(os.path.curdir + "/README.md")))
    print(
        "Is the current path a directory : " +
        str(os.path.isdir(os.path.curdir)))


def change_directories():
    current_directory = os.getcwd()
    os.chdir(os.path.join("/Users", "vchidamb", "Softwares"))
    print("Directory change success, current working directory is " + os.getcwd())
    os.chdir(current_directory)
    print("Back to original directory now : " + os.getcwd())


def print_directory_contents(dir_path):
    file_list = os.listdir(dir_path)
    print("List of directories in : " + dir_path)
    for file_name in file_list:
        print(file_name)

    print("End list!")

def path_join():
  path_str = os.path.join("Users", "vchidamb", "Softwares")
  print(path_str)

def check_path_exists(path):
    print("Does path exist? : " + str(os.path.exists(path)))

def walk_directory():
    tuple_structure = os.walk("../../learn-python")
    #For each folder name in the tuple structure walk through each subdirectory
    for folder_name, subdirectory, filenames in tuple_structure:
        print("The current foldername is : " + folder_name)
        for directory_name in subdirectory:
            print("The subdirectory names are : " + directory_name)
        for current_file in filenames:
            print("The current file name is : " + current_file)

def demo():
    print_current_working_directory()
    print_path_functions()
    path_join()
    change_directories()
    check_path_exists(os.path.join("/Users", "vchidamb", "does_not_exist"))
    print_directory_contents(os.getcwd())
    walk_directory()

demo()


