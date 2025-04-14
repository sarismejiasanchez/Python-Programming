# PARENT CLASSESS VS CHILD CLASSES

# Parent Class
class Parent:
    def __init__(self):
        self.a = 7

# Empty Child Class
class Child(Parent):
    pass

# Child class instance
c = Child()

# Inherited attribute from Parent class
print(c.a)  # Output: 7

# Change the value of the inherited attribute
c.a = 10
# Print the changed value
print(c.a)  # Output: 10


# # EMPLOYEES, SUPERVISORS, AND CHEFS CLASSES
class Employees():
    """
    Employees class serves as the base class for all employees.
    
    Attributes:
        name (str): The first name of the employee.
        surname (str): The last name of the employee.
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Supervisors(Employees):
    """
    Supervisors class inherits from the Employees class and adds a password attribute.
    
    Attributes:
        name (str): The first name of the supervisor (inherited from Employees).
        surname (str): The last name of the supervisor (inherited from Employees).
        password (str): The password for the supervisor.
    """
    def __init__(self, name, surname, password):
        super().__init__(name, surname)
        self.password = password

class Chefs(Employees):
    """
    Chefs class inherits from the Employees class and adds a method for leave requests.
    
    Attributes:
        name (str): The first name of the chef (inherited from Employees).
        surname (str): The last name of the chef (inherited from Employees).
    
    Methods:
        leave_request(days: int) -> str:
            Returns a string requesting leave for a specified number of days.
    """
    def leave_request(self, days):
        return f"May I take a leave for {days} days"

# Creating instance of Supervisors
adrian = Supervisors("Adrian", "Smith", "P@ssw0rd")

# Creating instances of Chefs
emily = Chefs("Emily", "Jones")
juno = Chefs("Juno", "Doe")

# Accessing attributes of the Chefs class
print(f"{emily.name}, {emily.leave_request(5)}") # Emily, May I take a leave for 5 days

# Accessing attributes of the Supervisors class
print(f"{adrian.name} password: {adrian.password}") # Adrian password: P@ssw0rd


# INHERITANCE AND MULTIPLE INHERITANCE

# Simple Inheritance
class A:
    """
    A base class with no attributes or methods.
    """
    pass

class B(A):
    """
    A class that inherits from class A.
    Demonstrates simple inheritance.
    """
    pass

# Multiple Inheritance
class A:
    """
    A base class with a single attribute `a`.
    """
    a = 1

class B:
    """
    A base class with a single attribute `b`.
    """
    b = 2

class C(A, B):
    """
    A class that inherits from both A and B.
    Demonstrates multiple inheritance.
    """
    pass

# Example of multiple inheritance
c = C()
print(c.a, c.b)  # Output: 1 2

# Inheritance of multiple levels
class B(A):
    """
    A class that inherits from A and overrides the attribute `a`.
    """
    a = 2

class C(B):
    """
    A class that inherits from B.
    Demonstrates inheritance across multiple levels.
    """
    pass

# Example of multi-level inheritance
c = C()
print(c.a)  # Output: 2   

# Integrated functions
# issubclass()
print(f"Is A a subclass of B?: {issubclass(A, B)}")  # Output: Is A a subclass of B?: False
print(f"Is B a subclass of A?: {issubclass(B, A)}")  # Output: Is B a subclass of A?: True

# isinstance()
class A:
    """
    A base class with no attributes or methods.
    """
    pass

class B(A):
    """
    A class that inherits from A.
    """
    pass

# Example of isinstance()
b = B()
print(f"Is b an instance of B?: {isinstance(b, B)}")  # Output: Is b an instance of B?: True
print(f"Is b an instance of A?: {isinstance(b, A)}")  # Output: Is b an instance of A?: True

# super()
class Fruit:
    """
    A base class representing a fruit.

    Attributes:
        fruit (str): The type of fruit.
    """
    def __init__(self, fruit):
        print(f"Fruit type: {fruit}")

class FruitFlavor(Fruit):
    """
    A class that inherits from Fruit and adds a flavor attribute.

    Attributes:
        fruit (str): The type of fruit (inherited from Fruit).
        flavor (str): The flavor of the fruit.
    """
    def __init__(self, fruit, flavor):
        super().__init__(fruit)
        print(f"{fruit} is {flavor}")

# Example of using super()
# Creating an instance of FruitFlavor
apple = FruitFlavor("Apple", "sweet")  # Output: Fruit type: Apple \n Apple is sweet
orange = FruitFlavor("Orange", "citrusy")  # Output: Fruit type: Orange \n Orange is citrusy
