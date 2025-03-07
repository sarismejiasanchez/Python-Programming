# LOOPING
# Looping is used to iterate through the sequence and access each item inside the sequence. 

# For loop
# To declare a For loop, I used the -for- key word.
# I now need a variable to put the value into. In this case I used the variable -item-.
# I also use the -in- keyword to specify where I want to loop over.
# Sequence: The sequence that we want to iterate through. In this case, I used the -str- variable.
# The sequence can be a string, list, tuple, or dictionary.

# item: The variable item is a placeholder that will store the current letter in the sequence.
# str: The sequence that we want to iterate through.

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

# For loop with range function
# It's important to note the three main points.
# The iteration starts 0. The reason for that is that it's the first item in an array or the first item in the index. 
for i in range(10): # Range function
    print("Looping...", i)

# In this case, item calls each of the five dessert titles in turn and our print statement combines them into a sentence.
favorites = ["Creme Brule", "Apple Pie", "Churros", "Tiramisu", "Chocolate Cake"]

for desert in favorites:
    print(f"I like this desert: {desert}")

# It's important to note that In a standard for loop, I don't have access to the index, 
# but I can use the enumerate function to do that.

# Obtain the index of each item in the sequence using the enumerate function.
for idx, item in enumerate(favorites):
    print(f"{idx} = {item}")
    
# While loop
# The while loop is used to iterate through a block of code as long as the condition is true.
# The condition is evaluated before executing the code block.
count = 0

while count < len(favorites):
    print(f"I like this desert: {favorites[count]}")
    count += 1
    