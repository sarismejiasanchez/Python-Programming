# Exercise: Control Flows and Loops to solve a problem

"""Introduction

In this exercise, you will practice control flow with loops to solve problems. You will be given a list of integers and need to add some code to find a specific number in the list and return it.

Instructions
1.	In num_list, create a new “for” loop and print each value in the list sequentially.
2.	Inside the “for” loop, create a condition that searches for all numbers greater than 45 and prints only those numbers that meet this condition.
3.	Change the “print” statement to "More than 45" and add an “else” condition with a “print” statement saying "Less than 45".
4.	Update the “for” loop to use the enumerate function to obtain and use the index. Modify the condition to search for the number 36 and print the following:
"Number found at position:", index number.
5.	Next, create a new variable named "count", assign it the value 0, and place it outside the “for” loop.
6.	Inside the “for” loop, increment the counter by 1.
7.	Add a “print” statement outside the “for” loop to print the value of the "count" variable.
8.	Finally, add a “break” statement immediately after the “print” statement inside the “if” condition that finds the number.
"""

num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

print("STEP 1")
# 1. Print each value in the list sequentially
for number in num_list:
    print(number)

print("STEP 2")
# 2. Print only numbers greater than 45
for number in num_list:
    if number > 45:
        print(number)

print("STEP 3")
# 3. Print "More than 45" or "Less than 45"
for number in num_list:
    if number > 45:
        print("More than 45")
    else:
        print("Less than 45")

print("STEP 4")
# 4. Print the position of the number 36
for index, number in enumerate(num_list):
    if number == 36:
        print("Number found at position:", index)

print("STEPS 5, 6, 7")
# 5. Create a new variable named "count" and assign it the value 0 outside the "for" loop
count = 0

for index, number in enumerate(num_list):
    # 6. Increment the counter by 1 inside the "for" loop
    count += 1
    if number == 36:
        print("Number found at position:", index)

# 7. Print the value of the "count" variable outside the "for" loop
print(count)

print("STEP 8")
# 5. Create a new variable named "count" and assign it the value 0 outside the "for" loop
count = 0

for index, number in enumerate(num_list):
    # 6. Increment the counter by 1 inside the "for" loop
    count += 1
    if number == 36:
        print("Number found at position:", index)
        # 8. Add a "break" statement immediately after the "print" statement
        break

# 7. Print the value of the "count" variable outside the "for" loop
print(count)