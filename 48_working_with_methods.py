# WORKING WITH METHODS: EXERCISES

# Example 1:
class A:
    def a(self):
        return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B, A):
    pass

# Driver code
c = C()
print(c.a()) # Function inside B
print(C.mro()) # [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# The C class inherits from B and A, and the method a() is defined in both classes.
# When we call c.a(), it resolves to the method in class B because B is listed first in the inheritance order.

# Class "C" inherits from classes "B" and "A". When I don't find a function "a()" inside class "C", 
# I should search in classes "B" and "A", and it's important to do it in that order

# Example 2:
class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    def b(self):
        return "Function inside C"
        pass

class D(C):
    pass

d = D()
print(d.b()) # Function inside C
print(D.mro()) # [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# The D class inherits from C, which has its own implementation of the method b().
# When we call d.b(), it resolves to the method in class C because D does not override it.

# Class "D" inherits from class "C", which in turn inherits from classes "A" and "B". 
# Class "D" accesses the immediate superclass of class "D", which is class "C", 
# and resolves the value of the variable once it is found in that superclass.

# Now let's say that I comment out the declaration inside class "C".
class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    # def b(self):
        # return "Function inside C"
    pass

class D(C):
    pass

d = D()
print(d.b()) # Function inside A
print(D.mro()) # [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# The D class inherits from C, which in turn inherits from A and B.

# Since there was no value present inside class "C", the call to the previous function would go to "A". 
# This is because class "C" will point to class "A" as the higher priority when inheriting.

# Example 3:
class A:
    def c(self):
        return "Function inside A"

class B:
    def c(self):
        return "Function inside B"

class C(A, B):
    def c(self):
        return "Function inside C"

# class D(A, C):
     # pass

# d = D()
# print(d.a)

# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, C

# Note that this generates an error. In the previous code, class "D" inherits from both class "A" and class "C". 
# Class "C" is its immediate superclass, but since this is multiple inheritance, the rules are more complicated, 
# and you also need to check the priority of the classes passed to it.

# In this specific case, class "D" is unable to resolve the order that should be 
# followed while resolving the value of the variable in cases where the variable 
# is not present in the given object's class.

# The result is a "TypeError" because it is unable to create a method resolution order (MRO). 
# The MRO is Python's way of resolving the priority order of classes when dealing with inheritance.

# Example 4:
class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"

class C:
    def d(self):
        return "Function inside C"

class D(A, B):
    def d(self):
        return "Function inside D"

class E(B, C):
    def d(self):
        return "Function inside E"

class F(E, D, C):
    pass

f = F()
print(f.d()) # Function inside E
print(F.mro()) # [<class '__main__.F'>, <class '__main__.E'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

# The F class inherits from E, D, and C. 
# The code here is simple. Class "F" directly inherits from its immediate superclass and the first class passed to it. 
# Then, the second line shows what the "mro()" function returns.

# The examples in this reading demonstrate how code using multiple inheritance can become complicated and messy very quickly.
# Multiple inheritance, with all the advantages and flexibility it provides, 
# should only be used if you have a solid command of Python as a language to avoid creating "spaghetti code" 
# that is difficult to understand and maintain.
