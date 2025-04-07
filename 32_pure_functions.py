# TRADITIONAL AND PURE FUNCTIONS
# Pure functions will always do the same thing and return the same results no matter how many times they are called.
# Functional programming is a programming paradigm that utilizes functions for clean, consistent, and maintainable code.
# Compared to object-oriented programming, functional programming differs by design.

"""
This module explains the differences between traditional and pure functions in Python.
It also highlights the principles of functional programming.
"""

# Key differences between traditional and pure functions:
# - Traditional functions can access and modify variables in the global state, but pure functions cannot.
# - Both traditional and pure functions can access variables in the local state.
# - Traditional functions can change arguments, whereas pure functions cannot.
# - The outputs of traditional functions do not always depend on inputs, but the outputs of pure functions always do.

# Benefits of pure functions:
# 1. Known outcome: Always know what the outcome will be.
# 2. Consistent and reliable: Are consistent snippets of code that do exactly what they are intended to do.
# 3. Cache: Include the ability to cache since you know the return is always going to be the same.
# Multi-threaded programs: Will help prevent changes on the global scope ensuring data stays reliable.

# Pure function or not?
# Global Scope
global_list = [1, 2, 3]

def add_to(item):
    return global_list.append(item)

add_to(4) # The function modifies the global_list by appending the item passed as an argument.
print(global_list)  # Output: [1, 2, 3, 4]

# What do you think? Is this a pure function?
# No, it's not a pure function as it changes the global_list by appending the item which is passed as an argument.

# In order to change it to a pure function, you need to think how to extend the function to accept a list as an argument, 
# add the item to the list without modifying the original list, and how to return a new list with the newly added item.

# Acept list as an argument
# Original list intact
# Return new list

# Change to a pure function

def add_to_list(lst, item): # # Acept list as an argument
    new_list = lst.copy()  # Original list intact
    new_list.append(item)   # Append item to new list
    return new_list # Return new list

# Call the function
new_list = add_to_list(global_list, 4)
print(new_list)  # Output: [1, 2, 3, 4]
# The original list is unchanged
print(global_list)  # Output: [1, 2, 3]


