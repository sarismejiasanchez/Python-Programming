# *ARGS
# *args is used to pass a variable number of non-keyworded arguments to a function.
# The syntax is to use the symbol * before the parameter name that holds the values of all nonkeyword arguments.

# Function with 2 arguments
def sum_of(a, b):
    return a + b

print(sum_of(4, 5)) # 9

# TypeError: sum_of() takes 2 positional arguments but 3 were given
# print(sum_of(4, 5, 6)) 

# Function with *args to accept any number of arguments
def sum_of(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_of(4, 5, 6, 4, 5, 6)) # 30

# A more concise way to write the above function
def sum_of(*args):
    return sum(args)

print(sum_of(4, 5, 6, 7)) # 22
