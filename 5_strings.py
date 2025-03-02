# String
# A string is a sequence of characters enclosed in single or double quotes.

example_string = 'We are open'
print(example_string)
print(type(example_string))

example_string = "24 hours a day!"
print(example_string)
print(type(example_string))

# Multiline String
multiline_string = "This is \
to big to fit \
on a single line \
so we multi-lined it."

print(multiline_string)

multiline_string = "This is " \
                    "to big to fit " \
                    "on a single line " \
                    "so we multi-lined it."

print(multiline_string)

# Reassigning a string value
example_string = "We are closed"
print(example_string)

# Strings can be indexed using the [] operator.
print(example_string[9])  # 'o'
print(example_string[-1])  # 'd'
print(example_string[0])  # 'W'

# Length of a string
length = len(example_string)
print(length)


# Strings can be concatenated using the + operator.
a = "my favorite food is "
b = "mashed potatoes"
print(a + b)

# Strings can be repeated using the * operator.
# Strings can be sliced using the [start:stop:step] operator.
# Strings can be formatted using the format() method or f-strings.
# Strings can be compared using the ==, !=, <, <=, >, and >= operators.
# Strings can be checked for containment using the in and not in operators.
# Strings can be converted to uppercase using the upper() method.
# Strings can be converted to lowercase using the lower() method.
# Strings can be stripped using the strip() method.
# Strings can be split using the split() method.
# Strings can be joined using the join() method.
# Strings can be replaced using the replace() method.
# Strings can be formatted using the % operator.
