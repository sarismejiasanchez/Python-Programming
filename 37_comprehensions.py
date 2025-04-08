# COMPREHENSIONS

# 1. List Comprehensions
# The syntax for list comprehensions is:
# [<expression> for <item> in <sequence> if <condition>]
# [expression for item in iterable if condition]

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(f"Original list: {data}") # Original list: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Example 1: Listh comprehension: updating the same list
data = [x + 3 for x in data]
print(f"Updating the list: {data}") # Updating the list: [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]

# Example 2: List comprehension: creating a different list with updated values
new_data = [x * 2 for x in data]
print(f"Creating a new list: {new_data}") # Creating a new list: [10, 12, 16, 20, 28, 32, 40, 44, 52, 64, 68]

# Example 3: With an if condition: Multiples of 4
four_multiples = [x for x in new_data if x % 4 == 0]
print(f"Multiples of 4: {four_multiples}") # Multiples of 4: [12, 16, 20, 28, 32, 40, 44, 52, 64, 68]

# Example 4: Alternatively, we can update the list with the if condition as well
four_multiples_updated = [x - 1 for x in new_data if x % 4 == 0]
print(f"Multiples of 4 (minus 1): {four_multiples_updated}") # Multiples of 4 (minus 1): [11, 15, 19, 27, 31, 39, 43, 51, 63, 67]

# Example 5: Using range() function
nines = [x for x in range(100) if x % 9 == 0]
print(f"Multiples of 9: {nines}") # Multiples of 9: [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]

# Example 5: Using regular for loop
nines = []
for x in range(100):
    if x % 9 == 0:
        nines.append(x)
print(f"Multiples of 9 (using regular loop): {nines}") 
# Multiples of 9 (using regular loop): [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]

# Example 1: Using regular for loop
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
for x in range(len(data)):
    data[x] = data[x] + 3
print(f"Updating the list (using regular loop): {data}") 
# Updating the list (using regular loop): [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]

# 2. Dictionary Comprehensions
# The syntax for dictionary comprehensions is:
# {<key>: <value> for <key>, <value> in <sequence> if <condition>}