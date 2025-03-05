# LOOPING
# Looping is used to iterate through the sequence and access each item inside the sequence. 

# For loop
str = "Looping" # String is a sequence of characters

# item: The variable item is a placeholder that will store the current letter in the sequence.
# str: The sequence that we want to iterate through.
for item in str:    # Iterate through each character in the string
    print(item)

# You may also recall that you can access any character in the sequence by its index.
print(str[0])   # The first item in the sequence is 'L' and accessed withindex 0.
# Other items can be accessed with following items.

for item in str:
    # index = str.index(item)
    # value = item
    print(f"{item} = {str.index(item)}")

# While loop