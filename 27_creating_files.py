# CREATING FILES

# Files used to permanently store data so it is
# available for future use or as a permanent record.

# Creating a newfile.txt file and writing to it.
# This replaces the content of the file if it already exists.
with open("newfile.txt", "w") as file: # We can use mode = "w" or just "w" to indicate the mode.
    file.write("This is a new file created by Python!") # Writing a single line to the file.
    # Writing multiple lines to the file.
    # \n is used to create a new line.
    file.writelines(["\nThis is the second line.", "\nThis is the third line."])

# Append data to the end of the file.
# This mode does not overwrite the file.
with open("newfile.txt", "a") as file:
    file.writelines(["\nThis is the fourth line.", "\nThis is the fifth line."])

# Although mode = "a" creates the file if it does not exist, 
# this does not apply when the directory in the path does not exist; 
# in this case, it does generate an error.
try:
    with open("sample/newfile.txt", "a") as file:
        file.writelines(["\nThis is the sixth line.", "\nThis is the seventh line."])
except FileNotFoundError as e:
    print("Error:", e)