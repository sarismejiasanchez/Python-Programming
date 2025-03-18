# ERRORS AND EXCEPTIONS

# Syntax Error
# Caused by human error, usually cause by developer mistakes.
# Misspellings, missing colons, missing parenthesis, etc.

#     greeting = "Hello" # IndentationError: unexpected indent
# if greeting == "hello" # SyntaxError: expected ':'


# Exceptions
# Known errors that need to be handled.
# Happen during code execution.

# ZeroDivisionError: division by zero
# result = 5 /0 

def divide_by(a, b):
    return a / b

print(divide_by(40, 4)) # 10.0

# ZeroDivisionError: division by zero
# print(divide_by(40, 0))

# Exception Handling
# Try and Except blocks

def divide_by(a, b):
    return a / b

# The try statement will try and execute the code that you added inside it.
# If an exception occurs, the code inside the except block will be executed.
try:
    ans = divide_by(40, 0)
except Exception as e:
    print("Something went wrong!", e) # Something went wrong! division by zero
    print(e.__class__) # <class 'ZeroDivisionError'>

# More especific feedback to the end user.
try:
    ans = divide_by(40, a)
except ZeroDivisionError as e:
    print(f"{e}, we cannot divide by zero.") # division by zero, we cannot divide by zero.
# Multiple except blocks
except Exception as e:
    print(f"Something went wrong, {e}") # Something went wrong, name 'a' is not defined. In this case ans = divide_by(40, a)

# IndexError
"""
The following code has an issue. It attempts to locate an element in the list that does not exist. 
When executing the code, an IndexError will be raised. 
Add exception handling to prevent the error and return a simpler message for the user, 
such as "The item does not exist in the list.

# Starter code
items = [1, 2, 3, 4, 5]
item = items[6] # IndexError: list index out of range
print(item)
"""
items = [1, 2, 3, 4, 5]
try:
    item = items[6]
    print(item)
except IndexError as e:
    print(f"{e}, the element does not exist.") # list index out of range, the element does not exist.

# ZeroDivisionError
"""
In mathematics, there are rules about dividing by zero. 
The following code attempts to do so and will raise a ZeroDivisionError. 
Add exception handling to return 0 instead of allowing the error to occur.

# Starter code
def divide_by(a, b):
    return a / b


ans = divide_by(40, 0)
print(ans)
"""
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return 0
    except Exception as e:
        return (f"{e}, something went wrong.")

ans = divide_by(40, 0)
print(ans) # 0

ans = divide_by(40, "a")
print(ans) # unsupported operand type(s) for /: 'int' and 'str', something went wrong.

# FileNotFoundError
"""
The following code searches for a file that does not exist. 
Add exception handling to catch this error and return the following message: 
"The file could not be found."

# Starter code
with open('file_does_not_exist.txt', 'r') as file:
    print(file.read())
"""
try:
    with open("file_does_not_exist.txt", "r") as file:
        print(file.read())
except FileNotFoundError as e:
    print("The file could not be found.")

