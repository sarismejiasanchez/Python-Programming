# ABSTRACT CLASSES AND METHODS

# Abstract Class can have one or more abstract methods.
# Child of Abstract Class can only be instantiated if abstract methods are overriden.

# Import ABC from the abc module and abstractmethod decorator

# A decorator is a function that takes another function as its arguments 
# and gives a new function as its output.
from abc import ABC, abstractmethod

# Create inheriting class
class SomeAbstractClass(ABC):
    # Call abstract method
    @abstractmethod
    def someabstractmethod(self):
        pass

# An employer wants to collect donations from employees for a charitable cause
# 1. Import ABC and abstractmethod
from abc import ABC, abstractmethod

# 2. Define ABC method
class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass

# 3. Create sub class
class Donation(Employee):
    def donate(self):
        # Implementation
        a = input("How much would you like to donate?: ")
        return a

# 4. Create instances and list amounts
amounts = []
jhon = Donation()
j = jhon.donate()
amounts.append(j)

peter = Donation()
p = peter.donate()
amounts.append(p)

# Print amounts
total_amount = sum(float(i) for i in amounts)
print(f"The total amount of donations is: {total_amount}")
