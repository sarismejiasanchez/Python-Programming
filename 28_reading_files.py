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
with open("C:/Users/username/Documents/newfile.txt", "r") as file:
    content = file.read()
    print(content)

# Relative path
with open("../Documents/newfile.txt", "r") as file:
    content = file.read()
    print(content)

# Example of reading a file from a different directory
# Up two levels from the current directory
with open("../../newfile.txt", "r") as file:
    content = file.read()
    print(content)
