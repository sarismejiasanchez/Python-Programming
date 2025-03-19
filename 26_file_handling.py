# FILE HANDLING FUNCTIONS
"""
1. open()
The open function is used for reading, writing and creating files.
The open function accepts two arguments:
- The first is the file name or the file location.
- The second is the mode. 
The mode indicate what action is required such as reading, writing or creating a file.
Its also specifies if you want the file output in text or binary format.

open("file_name" "file_location", "mode")

Mode sets:
"r" - Open and Read (text format)
"rb" - Open and Read (binary format)
"r+" - Open for reading and writing (text format)
"w" - Open for writing, this mode overwrites the existing file or creates a new file if it does not exist (text format)
"a" - Open for editing or appending data to the end of the file (text format)


2. close()
The close function is used for closing the open file connection.
That it does not take any arguments.

3. with open()
There is one more way to open and close a file in Python.
The advantage os using it is that it closes the file automatically.

with open("file_name", "mode") as file:

- Diferences between opening a file in text and binary mode:
- Text format is more user friendly because humans can read it. This is the default format.
- Binary format is more compact and therefore result in better performance. 
Add "b" to the mode to open a file in binary format.
"""

# Add a read line or read lines function
# readline() - return the first line of the file
# readlines() - return all the lines of the file
file = open("test.txt", mode = "r")
data = file.readline() # Read the first line of the file
print(f"open(): {data}") # Print the first line of the file
file.close() # Close the file

# with open() function
with open("test.txt", mode = "r") as file:
    data = file.readline()
    print(f"with open(): {data}")