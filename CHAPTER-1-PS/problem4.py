#Write a python program to print the contents of a directory using the os module Search online for the function which does that. 

import os

def print_directory_contents(directory):
    try:
        contents = os.listdir(directory)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Directory not found.")

# Specify the directory you want to print
directory_path = '/New Volume'
print_directory_contents(directory_path)
