# KWARGS

def sum_of(*args):
    return sum(args)

# Calculate a total bill for a restaurant
# sum_of() got an unexpected keyword argument 'coffee'
# total_bill = sum_of(coffee = 2.99, cake = 4.55, juice = 2.99)

# **KWARGS
# **kwargs allows you to pass keyworded variable length of arguments to a function.
# You should use **kwargs if you want to handle named arguments in a function.
# The syntax is to use the double asterisk ** before the parameter name that holds the values of all keyword arguments.


# for key, value in kwargs.items():
def sum_of(**kwargs):
    total = 0
    for product, price in kwargs.items():
        total += price
    return round(total, 2) # round to 2 decimal places

total_bill = sum_of(coffee = 2.99, cake = 4.55, juice = 2.99)
print(f"Total bill: ${total_bill}") # Total bill: $10.53

# A more concise way to write the above function, for values only
def sum_of(**kwargs):
    total = 0
    for price in kwargs.values():
        total += price
    return round(total, 2)

total_bill = sum_of(coffee = 2.99, cake = 4.55, juice = 2.99)
print(f"Total bill: ${total_bill}") # Total bill: $10.53

# A more concise way to write the above function, using the sum() function with values only
def sum_of(**kwargs):
    return round(sum(kwargs.values()), 2) # round to 2 decimal places

total_bill = sum_of(coffee = 2.99, cake = 4.55, juice = 2.99)
print(f"Total bill: ${total_bill}") # Total bill: $10.53
