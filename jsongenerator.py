'''
Introduction
So far, you have learned the different ways you can use import statements to import other Python files, modules, and packages. You have also seen the different ways you can import specific functions using different import formats.

Goal
Use the import statement to import a built-in Python package.
Use the import statement to call a function present in another Python file.

Objectives
    Learn how to use import to bring external code into the direct scope of the project.

Instructions:
Step 1: Open the jsongenerator.py file present inside the project folder.
Step 2: Import a built-in package called json.
Step 3: Import the following from a file called employee.py:
        - A function called details
        - Variables called employee_name, age, and title
Step 4: Implement the create_dict() function that returns a dictionary given the employee information.
    4.1 Create and return a dictionary with three key-value pairs where
        the keys are string variables - "first_name", "age", and "title" and their respective values are the variables employee_name, age, and title that we imported from the employee module. 
        Make sure to cast the values to the expected types.
Step 5:
        Use a function called "dumps()" from the "json" module using dot notation and pass it 
        the employee_dict dictionary that we created. Return its value to a variable called json_object.
        The format should look like this:
        variable = json.dumps(dict)
Step 6: Complete the write_json_to_file() function
    6.1 Use a built-in function called "open()" and pass it the output_file argument and "w". 
        Return the value of this function to a variable called newfile.
    6.2 Call a function called "write()" on this "newfile" variable. 
        Pass the json_object variable you created in step 5 into it.
    6.3 Close this file by calling a built-in function "close()" directly on newfile. 
        You don't need to pass any arguments here. (Note: Using 'with open(...)' handles closing automatically).
Step 7: Save the files.
Step 8: Open the terminal to run the files.

Import statements:
    1. Import the built-in json python package
    2. From employee.py, import the details function and the employee_name, age, title variables
'''

### WRITE IMPORT STATEMENTS HERE
import json
from employee import details, employee_name, age, title

def create_dict(name, age, title):
    """ Creates a dictionary that stores an employee's information

    [IMPLEMENT ME]
        1. Return a dictionary that maps "first_name" to name, "age" to age, and "title" to title

    Args:
        name: Name of employee
        age: Age of employee
        title: Title of employee

    Returns:
        dict - A dictionary that maps "first_name", "age", and "title" to the
                name, age, and title arguments, respectively. Make sure that 
                the values are typecasted correctly (name - string, age - int, 
                title - string)
    """
    ### WRITE SOLUTION HERE
    # Create a dictionary to store employee information
    employee_dict = {}
    employee_dict["first_name"] = str(name)
    employee_dict["age"] = int(age)
    employee_dict["title"] = str(title)
    
    # Return the dictionary
    return employee_dict
    
    raise NotImplementedError()

def write_json_to_file(json_obj, output_file):
    """ Write json string to file

    [IMPLEMENT ME]
        1. Open a new file defined by output_file
        2. Write json_obj to the new file

    Args:
        json_obj: json string containing employee information
        output_file: the file the json is being written to
    """
    ### WRITE SOLUTION HERE
    # Open the file in write mode
    with open(output_file, 'w') as file:
        # Write the json object to the file
        file.write(json_obj)

    return output_file

    raise NotImplementedError()

def main():
    # Print the contents of details() -- This should print the details of an employee
    details()

    # Create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    ''' 
    Use a function called dumps from the json module to convert employee_dict
    into a json string and store it in a variable called json_object.
    '''
    ### WRITE YOUR CODE BY MODIFYING THE LINE BELOW
    # In the line below replace the None keyword with your code. 
    # The format should look like: variable = json.dumps(dict)
    
    # Convert the employee_dict to a json string
    json_object = json.dumps(employee_dict)
    
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()