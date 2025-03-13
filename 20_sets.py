# SETS
# Sets are unordered collections of unique elements. 
# it's also a collection of unaltered items.

# Sets are defined by values separated by curly braces {}.
my_set = {1, 2, 3, 4, 5, 5} 
print(my_set) # {1, 2, 3, 4, 5} omitting the duplicate 5
print(type(my_set)) # <class 'set'>

# We also can construct them by using the set() function.
my_set = set([2, 4, 6, 8, 4])
print(my_set) # {8, 2, 4, 6} omitting the duplicate 4
print(type(my_set)) # <class 'set'>

# Add elements to a set
my_set.add(10)
print(my_set) # {2, 4, 6, 8, 10}

# Remove elements from a set (if the element is not present, it raises a KeyError)
my_set.remove(4)
print(my_set) # {2, 6, 8, 10}

# KeyError: 12
# my_set.remove(12) 

# Discard elements from a set (if the element is not present, it does nothing)
my_set.discard(2)
print(my_set) # {6, 8, 10}

my_set.discard(12) # does nothing
print(my_set) # {6, 8, 10}

# Math operations with sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union
union = set_a.union(set_b) # Omits the duplicates
print(f"Union: {union}") # Union: {1, 2, 3, 4, 5, 6, 7, 8}

# Union with the pipe operator
union = set_a | set_b
print(f"Union: {union}") # Same as above

# Intersection
intersection = set_a.intersection(set_b) # Only the common elements
print(f"Intersection: {intersection}") # Intersection: {4, 5}

# Intersection with the ampersand operator
intersection = set_a & set_b 
print(f"Intersection: {intersection}") # Same as above

# Difference
difference = set_a.difference(set_b) # Elements in set_a that are not in set_b
print(f"Difference: {difference}") # Difference: {1, 2, 3}

# Difference with the minus operator
difference = set_a - set_b
print(f"Difference: {difference}") # Same as above

# Symmetric difference
symmetric_difference = set_a.symmetric_difference(set_b) # Elements that are in set_a or set_b but not in both
print(f"Symmetric Difference: {symmetric_difference}") # Symmetric Difference: {1, 2, 3, 6, 7, 8}

# Symmetric difference with the caret operator
symmetric_difference = set_a ^ set_b
print(f"Symmetric Difference: {symmetric_difference}") # Same as above

# TypeError: 'set' object is not subscriptable
# this means that the set is not a sequence, it doesn't contain an ordered index of all elements inside.
# print(set_a[2])
