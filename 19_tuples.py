# TUPLES
# They're used as data structures and help to create solid, well performing code.
# To declare the tuple itself, I use parentheses. 
# A tuple can accept any mix of data types. 

my_tuple = (1, "strings", 3.5, True)

# To access any of the items within the tuple, I can use methods similar to those used with the list 
# by referring to an index. Remember Index always starts with zero.

print(my_tuple[1]) # strings

# Print the type of the tuple
print(type(my_tuple)) # <class 'tuple'>

# We could also declare a tuple without using the parentheses. 
# However, it's best practice to use the parentheses.
my_tuple = 1, "strings", 3.5, True, False, 1, 0
print(type(my_tuple)) # <class 'tuple'>

# Count method returns the number of times a specified value occurs in a tuple.
print(my_tuple.count(1)) # Returns 3 because True also has a value of 1
print(my_tuple.count(False)) # Returns 2 because False also has a value of 0
print(my_tuple.count(3.5)) # Returns 1
print(my_tuple.count("strings")) # Returns 1

# Index method returns the index of the first occurrence of the value.
print(my_tuple.index(True)) # 0, because 1 also has a value of True
print(my_tuple.index(False)) # 4
print(my_tuple.index("strings")) # 1
# ValueError: tuple.index(x): x not in tuple
# print(my_tuple.index("Strings")) 

print(my_tuple) # (1, 'strings', 3.5, True, False, 1, 0)
# Iterate through the tuple
for element in my_tuple:
    print(element)

# Iterate and print the index and the element
for index, element in enumerate(my_tuple):
    print(f"Index: {index}, Element: {element}")

# Unpacking a tuple
# Unpacking is a way to assign the elements of a tuple to multiple variables.
# The number of variables must match the number of elements in the tuple.
# If the number of variables is more or less than the number of elements in the tuple,
# Python will raise an error.

coordinates = (10, 20, 30)

# Unpacking the tuple
x, y, z = coordinates
print(x) # 10
print(y) # 20
print(z) # 30

# The tuple is immutable, meaning that once it's created, it cannot be changed.

# TypeError: 'tuple' object does not support item assignment
# my_tuple[2] = "Hello"
