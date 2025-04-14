# CLASSES AND INSTANCES

# Create a class, instantiate it, and access its attributes and methods

class Person:
    name = "John"
    age = 30
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person()
print(person1.name)  # Accessing the name attribute
print(person1.age)   # Accessing the age attribute
# Call the greet method
person1.greet()  # Output: Hello, my name is John and I am 30 years old.

# Class definition
class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    # Attributes of the class
    num_rooms = 5
    bathrooms = 2
    
    def cost_evaluation(self, rate):
        print(self.num_rooms)
        
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost

# Create an instance of the House class
house1 = House()
print(house1.num_rooms)  # Accessing the num_rooms attribute
print(House.num_rooms)   # Accessing the class attribute

# Update the num_rooms attribute of the house1 instance
house1.num_rooms = 7
print(house1.num_rooms) # Accessing the updated num_rooms attribute
print(House.num_rooms) # Accessing the class attribute

# Update the class attribute num_rooms
House.num_rooms = 7
print(house1.num_rooms) # Accessing the updated num_rooms attribute
print(House.num_rooms) # Accessing the class attribute

# What will be the output of running the following code?
value = 7
class A:
    value = 5
a = A()
a.value = 3
print(value) # Use the global variable
# The output will be 7, because use the global variable value

# What will be the output of running the following code?
bravo = 3
# b = B() 
# # NameError: name 'B' is not defined
class B:
    bravo = 5
    print("Inside class B")
c = B()
# print(b.bravo) 
# # NameError: name 'b' is not defined, because the instance b is not defined yet when we try to access its attribute

# The output will be Error: name 'B' is not defined, because the class B is not defined yet when we try to create an instance of it.