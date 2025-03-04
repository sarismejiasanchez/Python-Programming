# CONDITIONAL STATEMENTS
# if, elif, else

# if statement
# if condition proves to be True, the code block will be executed

# else statement
# if the condition proves to be False, the code block will be executed

# elif statement
# if the first condition proves to be False, the elif statement will be checked

# A restaurant wants to apply diffeerent discounts based on the amount its customer spent
bill_total = 210

discount_1 = 10
discount_2 = 20

if bill_total > 100 and bill_total < 200:
    print("Bill is greater than 100")
    bill_total = bill_total - discount_1
elif bill_total > 200:
    print("Bill is greater than 200")
    bill_total = bill_total - discount_2
else:
    print(f"Bill is less or equal to 100 or 200")

print(f"Total bill: {bill_total}")


# LOOPS
# for, while

# for loop
# check the condition and execute the code block until the condition is False