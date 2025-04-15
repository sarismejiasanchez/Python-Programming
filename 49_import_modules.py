# ACCESSING AND IMPORT MODULES

# Importing the sys module
import sys

locations = sys.path

# Print the list of locations where Python looks for modules
print("Locations where Python looks for modules:")
[print(f"- {location}") for location in locations]

# Importing the calendar module
import calendar

leapdays = calendar.leapdays(2000, 2025)
print(f"Leap days between 2000 and 2025: {leapdays}") # Leap days between 2000 and 2025: 7

isitleap = calendar.isleap(2025)
print(f"Is 2025 a leap year? {isitleap}") # Is 2025 a leap year? False


# Get the number of leap days in a range of years
year = 2025
month = 2
# Get the first weekday of the month and the number of days in the month
day_of_week, days_in_month = calendar.monthrange(year, month)
# Convert day number to day name
day_name = calendar.day_name[day_of_week]
# Convert month number to month name
month_name = calendar.month_name[month]

print(f"{month_name} 2025 starts on {day_name} and has {days_in_month} days.")


# Python has a standard library of available modules called built-in modules. 
# These modules are built directly into the Python interpreter and do not need to be installed separately.

# built-in modules are available for use as soon as you start the Python interpreter.
# https://docs.python.org/3.13/library/index.html

# The Python Package Index (PyPI) is a repository of software for the Python programming language.
# https://pypi.org/
# pip install <package_name>

# Import specific function from a module for will prevent overloading the interpreter
from math import sqrt, pi

# Use sqrt function from math module
root = sqrt(16)
print(f"Square root of 16 is {root}") # Square root of 16 is 4.0

# Use pi constant from math module
print(f"Value of pi is {pi}") # Value of pi is 3.141592653589793

# Importing a module with an alias
import random as rd
# Generate a random number between 1 and 10
random_number = rd.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}") # Random number between 1 and 10: 7

# Importing a module with an alias and using a specific function
from math import factorial as fact
factorial = fact(5)
print(f"Factorial of 5 is {factorial}") # Factorial of 5 is 120

# Importing multiple functions from a module
from math import sin, cos, tan
# Calculate sine, cosine, and tangent of 45 degrees
angle = 45
sine = sin(angle)
cosine = cos(angle)
tangent = tan(angle)
print(f"Sine of {angle} degrees is {sine}") # Sine of 45 degrees is 0.8509035245341184
print(f"Cosine of {angle} degrees is {cosine}") # Cosine of 45 degrees is 0.5253219888177297
print(f"Tangent of {angle} degrees is {tangent}") # Tangent of 45 degrees is 1.6197751905438615

# Importing all functions from a module
from datetime import *

# Now we can use all datetime functions without the module prefix

# Get the current date and time
current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}") # Current date and time: 2025-04-15 13:54:30.115343
# Get the current time zone
current_timezone = timezone.utc
print(f"Current time zone: {current_timezone}") # Current time zone: UTC

# Note: This approach is generally not recommended for large modules
# as it can lead to namespace pollution and make code less readable



# To import a .py file from the current working directory as a module:

# 1. Ensure the .py file you want to import is in the same directory
#    as the script that is importing it. Python searches the current directory for modules by default.
# 2. Use the 'import' statement followed by the filename (without the .py extension).
#    For example, if you have a file named 'my_module.py' in the same directory,
#    you can import it with:
#    import my_module
# 3. You can then access the functions, classes, or variables defined in 'my_module.py'
#    using dot notation:
#    my_module.my_function()
#    variable = my_module.my_variable
# Note: Filenames starting with numbers are not valid Python identifiers and 
# cannot be imported directly using the standard 'import' statement.
