# MATH OPERATORS

# Addition
result = 2 + 3
print(result)

# Subtraction
result = 3 - 1
print(result)

# Multiplication
result = 7 * 4
print(result)

# Division
result = 35 / 5
print(result)

# LOGICAL OPERATORS
# Use for control flow and decision making

a = 5

# and
# Checks if both conditions are true
result = a > 5 and a < 10
print(result) # False

# or
# Checks if at least one condition is true
result = a > 5 or a < 10
print(result) # True

# not
# Inverts the result
result = not(a > 5)
print(result) # True

# Example
loyalty_discount = 10
in_loyalty_program = True
total_bill = 200

if in_loyalty_program and total_bill > 100:
    total_bill = total_bill - loyalty_discount
    print(f"You have received a loyalty discount of ${loyalty_discount}. Your total bill is now ${total_bill}.")
