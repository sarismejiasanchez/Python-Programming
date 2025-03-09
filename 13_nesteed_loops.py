# Python nested loops can be used to solve more complex problems.

import time
start_time = time.time()

# Outer loop
for i in range(100): # Define the number of rows
    # Inner loop
    for j in range(1000): # Define the number of columns
        print(0, end = " ")
    print()

# The larger the array or the larger the range, in this case, the more time it's going to take for a program to complete. 
print(f"Seconds: {round(time.time() - start_time, 2)}")
print()

start_time = time.time()
# Outer loop
for i in range(1):
    # Inner loop
    for j in range(10):
        print(0, end = " ")
    print()

print(f"Seconds: {round(time.time() - start_time, 2)}")