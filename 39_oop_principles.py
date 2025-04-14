# Encapsulation

# Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP).
# It restricts direct access to certain components of an object and allows controlled access
# through public methods. This ensures data protection and enforces controlled interaction
# with the object's internal state.

# Key concepts of encapsulation:
# 1. Protected members: Indicated by a single underscore (_) at the beginning of the name.
#    These can be accessed outside the class but are intended to be used only within the class
#    or its subclasses. This is a convention, not a strict rule in Python.
# 2. Private members: Indicated by double underscores (__). These cannot be accessed directly
#    from outside the class due to name mangling, which changes the attribute's name internally.
# 3. Public methods: Used to access or modify private members in a controlled way, ensuring
#    that any necessary validations or logic are applied.

class EncapsulationExample:
    def __init__(self):
        self._protected_member = "I am a protected member"  # Protected member
        self.__private_member = "I am a private member"     # Private member

    def get_private_member(self):
        # Public method to access the private member
        return self.__private_member

    def set_private_member(self, value):
        # Public method to modify the private member
        self.__private_member = value


# Example usage
obj = EncapsulationExample()

# Accessing the protected member (not recommended, but possible)
print(obj._protected_member)

# Accessing the private member directly (this will raise an AttributeError)
# print(obj.__private_member)

# Accessing the private member through public methods
print(obj.get_private_member())
obj.set_private_member("New private value")
print(obj.get_private_member())

# Polymorphism

# Polymorphism is one of the core principles of Object-Oriented Programming (OOP).
# It allows the same operation, function, or method to behave differently depending on the type of object it is applied to.
# This makes code more flexible and reusable by enabling a single interface to handle different types of data.

# In this example:
# 1. The '*' operator behaves differently based on the type of the operand:
#    - For a string, it repeats the string a specified number of times.
#    - For an integer, it performs arithmetic multiplication.
#    - For a list, it repeats the elements of the list a specified number of times.
# 2. The 'len()' function also demonstrates polymorphism:
#    - For a string, it returns the number of characters in the string.
#    - For a list, it returns the number of elements in the list.

string = "poly"
num = 42
sequence = [1, 2, 3]

new_string = string * 3  # Repeats the string 3 times
new_num = num * 3        # Multiplies the integer by 3
new_sequence = sequence * 3  # Repeats the list 3 times

print(new_string, new_num, new_sequence)  # polypolypoly 126 [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(len(string))  # Returns the length of the string: 4
print(len(sequence))  # Returns the number of elements in the list: 3

# Inheritance

# Inheritance is one of the core principles of Object-Oriented Programming (OOP).
# It allows a class (child or derived class) to inherit attributes and methods from another class (parent or base class).
# This promotes code reuse and establishes a hierarchical relationship between classes.

# In this example:
# 1. The 'Animal' class is the base class that defines common attributes and methods for all animals.
# 2. The 'Dog' and 'Cat' classes are derived classes that inherit from the 'Animal' class.
#    - They override the 'speak' method to provide behavior specific to dogs and cats.
# 3. The '__init__' method of the 'Animal' class is reused in the derived classes, avoiding code duplication.
# 4. This demonstrates how inheritance allows for code reuse and specialization of behavior in child classes.

# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class (Child)
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Another derived class (Child)
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy barks.
print(cat.speak())  # Output: Whiskers meows.

from abc import ABC, abstractmethod

# Abstraction

# Abstraction is one of the core principles of Object-Oriented Programming (OOP).
# It focuses on hiding the internal implementation details of a class and exposing only the essential features.
# This allows users to interact with the object without needing to understand its internal workings.

# Key concepts of abstraction:
# 1. Abstract classes: These are classes that cannot be instantiated directly. They serve as blueprints for other classes.
# 2. Abstract methods: These are methods declared in an abstract class without implementation. 
#    Subclasses must provide their own implementation for these methods.

# Advantages of abstraction:
# - Hides implementation details, reducing complexity for the user.
# - Promotes code reusability by defining a common structure for related classes.
# - Makes code easier to maintain and extend by separating the interface from the implementation.

# In this example:
# 1. The 'Shape' class is an abstract class that defines a blueprint for all shapes.
# 2. It contains two abstract methods: 'area' and 'perimeter', which must be implemented by any subclass.
# 3. The 'Rectangle' and 'Circle' classes inherit from 'Shape' and provide specific implementations for the abstract methods.
# 4. This demonstrates how abstraction allows us to define a common interface for different shapes while hiding their specific implementations.

# Abstract class
class Shape(ABC):
    """
    Shape is an abstract class that defines a blueprint for all shapes.
    It contains an abstract method 'area' that must be implemented by derived classes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass

# Derived class: Rectangle
class Rectangle(Shape):
    """
    Rectangle is a concrete class that inherits from Shape.
    It implements the 'area' and 'perimeter' methods.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Derived class: Circle
class Circle(Shape):
    """
    Circle is a concrete class that inherits from Shape.
    It implements the 'area' and 'perimeter' methods.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Example usage
rectangle = Rectangle(5, 10)
circle = Circle(7)

print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 50
print(f"Rectangle Perimeter: {rectangle.perimeter()}")  # Output: Rectangle Perimeter: 30
print(f"Circle Area: {circle.area()}")  # Output: Circle Area: 153.93804
print(f"Circle Perimeter: {circle.perimeter()}")  # Output: Circle Perimeter: 43.98226