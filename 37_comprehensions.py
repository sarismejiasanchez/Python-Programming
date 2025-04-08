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

# Using range() function and not input list
using_range = {x: x * 2 for x in range(12)}
print(f"Using range(): {using_range}") 
# Using range(): {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22}

# Lists
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Using one input list
numDict = {x: x * 2 for x in numbers}
print(f"Using one input list: {numDict}")
# Using one input list: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22, 12: 24}

# Using two input lists
months_dict = {key: value for key, value in zip(numbers, months)}
print(f"Using two input lists: {months_dict}")
# Using two input lists: {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

# The syntax for dictionary comprehensions with two input lists is:
# {<key>: <value> for <key>, <value> in zip(<list1>, <list2>)}
# zip() function combines two lists into a list, 
months_dict = {key: value for key, value in zip(range(1, 12), months)}
print(f"Using two input lists (range): {months_dict}")
# Using two input lists (range): {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

# if the lists are of different lengths, 
# the length of resulting dictionary is iqual to the length of the shortest list.
# Example: Using rannge to 10 numbers for 12 months
# The dictionary resulting from the zip() function will have 10 elements
months_dict = {key: value for key, value in zip(range(1, 11), months)}
print(f"Mapping numbers to months (up to the shortest list): {months_dict}")
# Mapping numbers to months (up to the shortest list): {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct'}

# 3. Set Comprehensions
# The syntax for set comprehensions is:
# {<expression> for <item> in <sequence> if <condition>}
set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
print(f"Set comprehension: {set_a}") # Set comprehension: {10, 11, 13, 15, 17, 18, 19}

# 4. Generator Expressions
# Generator expressions are similar to list comprehensions, but they return a generator object instead of a list.

# The syntax for generator comprehensions is:
# (<expression> for <item> in <sequence> if <condition>)

# Benefits of Generator Objects:
# 1. Memory Efficiency:
#    Generators do not store all items in memory. Instead, they generate items one at a time, making them ideal for large datasets or infinite sequences.
# 2. Lazy Evaluation:
#    Generators compute values only when needed, which can save computational resources and improve performance.
# 3. Improved Performance:
#    By avoiding the creation of large data structures, generators reduce memory overhead and speed up execution.
# 4. Simplified Code:
#    Generator expressions provide a concise and readable way to create iterators.
# 5. Pipeline Processing:
#    Generators can be used in pipelines to process data step by step, passing intermediate results without storing them all at once.
# 6. Infinite Sequences:
#    Generators can represent infinite sequences (e.g., Fibonacci numbers, prime numbers) without running out of memory.

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)
print(f"Generator object: {gen_obj}") # Generator object: <generator object <genexpr> at 0x795030ae4b80>
print(type(gen_obj)) # <class 'generator'>

# Iterating over the generator object
for items in gen_obj:
    print(items, end=" ")  # Output: 2 3 5 7 11 13 17 19 23 29 31 

"""
When to Use Generators:
- When working with large datasets that cannot fit into memory.
- When you need to process data one item at a time.
- When you want to represent infinite sequences.
- When you want to improve performance by avoiding unnecessary computations or memory usage.
"""

def square(num):
    return num * num

# Map function
new_data = map(square, data)
new_data = list(new_data)
print(f"Map function (converted to list): {new_data}") 
# Map function (converted to list): [4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961]

# List comprehension
new_data = [square(x) for x in data]
print(f"List comprehension: {new_data}")
# List comprehension: [4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961]

# Practice assignment: Assigning key-value pairs to dictionary data structures
"""
1. What will be the output of the following code?
"[96][69]"
"[96],[69]"
[96][69]
"9669"
"""
a = [[96], [69]]
print("".join(list(map(str, a))))

result = "".join(list(map(str, a)))
print(type(result))
print(result) # [96][69]
# Initially, it will be a list of strings like ['[96]', '[69]'], which later becomes a single combined string.

"""
2. What will be the output of the following code?
['aa'], ['bb'], ['cc']
['aa', 'bb', 'cc'] 
['a', 'b', 'c']   
['alphaalpha', 'bravobravo', 'charliecharlie']                  
"""
z = ["alpha","bravo","charlie"]
new_z = [i[0] * 2 for i in z]
print(new_z) # ['aa', 'bb', 'cc']
# The output will be a list of strings.