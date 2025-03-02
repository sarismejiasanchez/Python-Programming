# NUMERIC DATA TYPES
# Integers, Floats, Complex

# Integers
number = 10
print(number)
print(type(number))

number = -10
print(number)
print(type(number))

# Floats
float_number = 10.5
print(float_number)
print(type(float_number))

# Complex
complex_number = 10 + 10j
print(complex_number)
print(type(complex_number))

# SEQUENCE DATA TYPES
# Strings, Lists, Tuples

# Strings
name = "John Doe"
print(name)
print(type(name))

name = 'John Doe'
print(name)
print(type(name))

# Lists
example_list = [1, 'hello', 4.5, "A"]
print(example_list)
print(type(example_list))

print(example_list[1]) # Accessing elements in a list

example_list[1] = 'world' # Modifying elements in a list
print(example_list[1]) 

# Tuples
example_tuple = (1, 'hello', 4.5, "A")
print(example_tuple)
print(type(example_tuple))

print(example_tuple[1]) # Accessing elements in a tuple

# example_tuple[1] = 'world' # TypeError: 'tuple' object does not support item assignment

# Dictionaries
ed = {'a': 22, 'b': 44.4}
print(ed)
print(type(ed))

print(ed['a']) # Accessing elements in a dictionary

ed['a'] = 33 # Modifying elements in a dictionary
print(ed['a'])
print(ed)

# BOOLEAN DATA TYPE
is_true = True
print(is_true)
print(type(is_true))

is_true = False
print(is_true)
print(type(is_true))

# SET DATA TYPE
example_set = {1, 'hello', 4.5, "A"}
print(example_set)
print(type(example_set))

example_set.add(1) # Adding elements to a set
print(example_set) # Duplicates are not allowed in a set
