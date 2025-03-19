# READ FILES

# 1. read()
# The read method returns the entire contents of the file as string
# that will contain all the characters.

with open("newfile.txt", "r") as file:
    content = file.read()
    print(content)

# You can also pass in an integer to return only the specified number of characters in the file.
with open("newfile.txt", "r") as file:
    lines = file.read(50) # read first 50 characters
    print(lines)
    
# 2. readline()
# Returns a single line as a string.
with open("newfile.txt", "r") as file:
    line = file.readline() # return the first line of the file
    print(line)

# Can also incluse an integer argument for returning an specified number of characters on a single line.
with open("newfile.txt", "r") as file:
    line = file.readline(30) # return the first 30 characters of the first line
    print(line)

# 3. readlines()
# Reads the entire contents of the file and returns it in an ordered list.
# This allows you to iterate over the list or pick out specific lines based on a condition.
with open("newfile.txt", "r") as file:
    content = file.readlines()
    print(len(content)) # number of lines in the file
    print(content) # print all the lines in the file
    
    for index, line in enumerate(content):
        # print(f"Linea {index + 1}: {line}")
        print(f"Línea {index + 1}: {line.strip()}") # Remove the newline character
    

# Reading files from Paths
"""
Files are stored in directories and they have paths.
Reading files from the same directory is straightforward, you only need the name of the file.

When working with different locations however, it's important that you know the difference 
between absolute and relative paths.

Absolute paths are the full path to the file, starting from the root directory.
Relative paths are the path to the file starting from the current directory.
"""

# Example of reading a file from a different directory
# Absolute path
try:
    with open("C:/Users/username/Documents/newfile.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
    
# Relative path
try:
    with open("../Documents/newfile.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
    
# Example of reading a file from a different directory
# Up two levels from the current directory
try:
    with open("../../newfile.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

"""
Storing file contents in data structures

Imagine you are trying to find a name for your new dog. You are not sure what you would like to call it, so you decide to use your Python knowledge to help you decide.
First, access a file (petnames.txt) containing a list of names you like for your new pet.
Now that you have the petnames.txt file, you would like to use it within your Python program to randomly select a single pet name.
You should read the file content and store the result in the variable f_content.
Then, f_content should be converted into a list using the split("\n") method, splitting the text by line breaks.
Then, import the random function and use the choice() method to randomly select a name.
"""

import random as rd

with open("petnames.txt", "r") as file:
    f_content = file.read()
    # print(f_content)
    f_content_list = f_content.split("\n") # Split the content of the file by new line
    # print(f_content_list)
    print(f"The name of your new pet is: {rd.choice(f_content_list)}") # The name of your new pet is: ...


# Reading files with user input
import random as rd
f_name = input("Type the file name: ")

with open(f_name) as file: # Ommited the mode "r" because it's the default mode
    f_content = file.read()
    f_content_list = f_content.split("\n")
    print(f"The name of your new pet is: {rd.choice(f_content_list)}")
    