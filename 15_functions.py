"""
At the most basic level, you can think of functions as a set of instructions 
that take an input and return and outputs.
A Python function is a modular piece of code that can be re-used repeatedly.
A function is declared using the def keyword followed by the name and task to complete. 
Optional parameters can also be added after the function name within a pair of parentheses.
"""

# Function to add two values
def sum(x, y):
    return x + y

x = 5
y = 4
print(f"The result of {x} + {y} is {sum(x, y)}")


# Calculate a tax amount for a customer, based on the total value of that bill.
bill = 175.00
tax_rate = 15
total_tax = (bill * tax_rate) / 100.00
print(f"Total tax: {total_tax}")

def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2) # round to 2 decimal places

print(f"Total Tax: {calculate_tax(175.00, 15)}")
print(f"Total Tax: {calculate_tax(164.33, 22)}")