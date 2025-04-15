# METHOD RESOLUTION ORDER

# Determines the order in wich a given method or attribute is resolved in a class hierarchy.
# The MRO is determined by the C3 linearization algorithm, which ensures that the order is consistent and respects the inheritance hierarchy.

# MRO attribute mro()
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())  # [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# Help funtion help()
class A:
    num = 5

class B(A):
    num = 9

class C(B):
    pass

print(help(C))

"""
Help on class C in module __main__:

class C(B)
    |  Method resolution order:
    |      C
    |      B
    |      A
    |      builtins.object
    |
    |  Data and other attributes inherited from B:
    |
    |  num = 9
    |
    |  ----------------------------------------------------------------------
    |  Data descriptors inherited from A:
    |
    |  __dict__
    |      dictionary for instance variables
    |
    |  __weakref__
    |      list of weak references to the object
"""
