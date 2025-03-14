# DICTIONARIES
# A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.

# With a Python dictionary, a key is assigned to a specific value. 
# This is called the key-value pair. 
# The key is used to retrieve the value, that is much faster than using lists.
# The dictionary is inmutable, so you can't change the key, but you can change the value.

# Declaring a dictionary
my_dict = {}
print(type(my_dict)) # <class 'dict'>

my_other_dict = dict()
print(type(my_other_dict)) # <class 'dict'>

# The key name can be a string, integer, or float.
dynamic_dict = {1: "Coffee", "2": "Tea", 3.0: "Juice"}
print(type(dynamic_dict)) # <class 'dict'>
print(f"dynamic_dict: {dynamic_dict}") # dynamic_dict: {1: 'Coffee', '2': 'Tea', 3.0: 'Juice'}

# Not does allow duplicate keys, if you try to add a key that already exists, the value will be updated.
print(f"Original dynamic_dict: {dynamic_dict}") # Original dynamic_dict: {1: 'Coffee', '2': 'Tea', 3.0: 'Juice'}
dynamic_dict = {1: "Coffee", "2": "Tea", 3.0: "Juice", 1: "Dessert"}
print(f"Updated dynamic_dict: {dynamic_dict}")# {1: 'Dessert', '2': 'Tea', 3.0: 'Juice'}

# Creating a dictionary with fromkeys() method
# The fromkeys() method returns a dictionary with the specified keys and the specified value.
keys = ["name", "age", "city"]
values = None
new_dict = dict.fromkeys(keys, values)
print(f"fromkeys type: {type(new_dict)}") # <class 'dict'>
print(f"fromkeys method: {new_dict}") # fromkeys method: {'name': None, 'age': None, 'city': None}

sample_dict = {1: "Coffee", 2: "Tea", 3: "Juice"}
print(type(sample_dict)) # <class 'dict'>
print(sample_dict) # {1: 'Coffee', 2: 'Tea', 3: 'Juice'}

# Accessing items
print(f"Accessing item with key 1: {sample_dict[1]}") # Accessing item with key 1: Coffee

# Add new key in dictionary with value None
sample_dict["dessert"] = None
print(f"Adding new key dessert: {sample_dict}") # Adding new key dessert: {1: 'Coffee', 2: 'Tea', 3: 'Juice', 'dessert': None}


# Updating items
# The structure to update an item in a dictionary is the same as accessing an item.
# The only difference is that you need to assign a new value to the key using the equals operator.
sample_dict["dessert"] = "Ice Cream"
print(f"Updating item dessert: {sample_dict}") # Updating item dessert: {1: 'Coffee', 2: 'Tea', 3: 'Juice', 'dessert': 'Ice Cream'}

sample_dict[2] = "Mint Tea"
print(f"Updating item with key 2: {sample_dict[2]}") # Updating item with key 2: Mint Tea

# Deleting items
# There are three methods to delete items from a dictionary:
# 1. Using the del keyword
# 2. Using the pop() method
# 3. Using popitem() method

# 1. Using the del keyword
# The del keyword removes the item with the specified key name.
# This method returns error if the key is not found.
# The del keyword can also delete the dictionary completely.
# This method not return any value.

print(f"Sample dictionary: {sample_dict}") # Sample dictionary: {1: 'Coffee', 2: 'Mint Tea', 3: 'Juice'}

del sample_dict[3] # Removing element 3: Juice from the dictionary
print(f"del mehod, key 3: {sample_dict}") # del mehod, key 3: {1: 'Coffee', 2: 'Mint Tea'}

# Generate key error if the key is not found
# KeyError: 4
# del sample_dict[4]

# Deleting the dictionary completely
del sample_dict
# NameError: name 'sample_dict' is not defined
# print(sample_dict) 

sample_dict = {1: "Coffee", 2: "Water", 3: "Milk", 4: "Water"}
print(f"Sample dictionary: {sample_dict}") # Sample dictionary: {1: 'Coffee', 2: 'Water', 3: 'Milk', 4: 'Water'}


# 2. Using the pop() method
# Remove the item with the specified key name and returns the value associated with the key.
# This method returns error if the key is not found.
# You can provide an optional default value to avoid the KeyError.

result = sample_dict.pop(4) # Removing element 4: Water from the dictionary
print(f"pop method, key 4: {result}") # pop method, key 4: Water
print(f"pop method, key 4: {sample_dict}") # pop method, key 4: {1: 'Coffee', 2: 'Water', 3: 'Milk'}

# KeyError: 4
# sample_dict.pop(4)

# Providing a default value
result = sample_dict.pop(4, "Not Found") # Not Found
print(f"pop method with default value, key 4: {result}") # pop method with default value, key 4: Not Found

result = sample_dict.pop(4, None) # None
print(f"pop method with default value, key 4: {result}") # pop method with default value, key 4: None

# 3. Using the popitem() method
# Remove the last item and returns a tuple with the key-value pair.

print(f"Sample dictionary: {sample_dict}") # Sample dictionary: {1: 'Coffee', 2: 'Water', 3: 'Milk'}

item = sample_dict.popitem()
print(f"popitem method: {item}") # popitem method: (3, 'Milk')
print(f"popitem method: {sample_dict}") # popitem method: {1: 'Coffee', 2: 'Water'}

# Clearing the dictionary
sample_dict.clear()
print(f"clear method: {sample_dict}") # clear method: {}

# KeyError: 'popitem(): dictionary is empty'
# sample_dict.popitem()

# PLUS
# Creating a dictionary with a zip() method
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]
zip_dict = dict(zip(keys, values))
print(f"zip method: {zip_dict}") # zip method: {'name': 'John', 'age': 30, 'city': 'New York'}

# Iterating through a dictionary

# Iterating through keys
for key in zip_dict:
    print(f"Key: {key}")

# Iterating through values
for value in zip_dict.values():
    print(f"Value: {value}")

# Iterating through key-value pairs
for key, value in zip_dict.items():
    print(f"{key}: {value}")

