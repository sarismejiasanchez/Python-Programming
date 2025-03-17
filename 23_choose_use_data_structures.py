# CHOOSE AND USE DATA STRUCTURES
import time

"""
This reading illustrates the importance of selecting the correct data structure for the task at hand.

Which data structure to choose?
The tricky part for new developers is understanding which data structure is suitable for the required solution.
Each data structure offers a different approach to storing, updating, and accessing the information stored within it.
Many factors can be considered, such as size, speed, and performance.
The best way to test and understand which one is more suitable is through an example.

Example: Employee list
In this example, there is a list of employees who work in a restaurant.
You need to be able to find an employee by their employee ID, a numeric-based ID.
The get_employee function contains a for loop to iterate over the employee list and returns an employee object if the ID matches.
"""

employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"}, 
    {"id": 12458, "name": "Paul", "department": "House Floor"}
    ]

def get_employee(id): 
    for employee in employee_list:
        if employee['id'] == id:
            return employee

# The time module is used to measure the time it takes to execute the code.
start_time = time.time()

print(get_employee(12458)); 
# {'id': 12458, 'name': 'Paul', 'department': 'House Floor'}

end_time = time.time()
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time of get_employee: {execution_time_ms:.3f} seconds")

"""
The code runs well and will return the user Paul since his ID, 12458, matches.
The challenge arises when the list gets larger.
Instead of two employees, you may have 2,000 or even 20,000.
The code will have to iterate through the list sequentially until the number matches.
The code could be optimized to split the search, but even then, it would still perform worse than other data structures, such as a dictionary.
"""

employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id];

start_time = time.time()

print(get_employee_from_dict(12458));
# {'id': '12458', 'name': 'Paul', 'department': 'House Floor'}

end_time = time.time()
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time of get_employee_from_dict: {execution_time_ms:.3f} seconds")

"""
Notice how, in this block of code, if you change the data structure to use a dictionary, it will allow you to find the employee.
The main difference is that you no longer need to iterate through the list to locate them.
If the list expands to a much larger size, the search time to find the employee remains the same.
This is a good example of how to choose the right data structure for the solution.
Both work well, but the balance to consider is time and scale.
The first solution will work well for small amounts of data, but it loses performance as the data increases.
The second solution is better suited for large amounts of data, as its structure allows for constant search time and thus accesses large amounts of data at a consistent speed.
This example shows that there is no one-size-fits-all solution and that the choice of data structure should be carefully considered based on the solution's constraints.
"""