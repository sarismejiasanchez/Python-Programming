"""
VARIABLE SCOPE
- The scope of a variable is the part of the program where the variable is recognized.
- Variables have a scope, which determines the visibility of the variable.
- The scope of a variable is the part of the program where the variable can be referenced/used.
- The purpose of scope is to protect the variable, so it does not get changed by other parts of the code. 

- Python has four types of variable scope, denoted by the LEGB rule:
    1. Local Scope
    2. Enclosing Scope
    3. Global Scope: Variables declared outside of a function or in global space.
    4. Built-in Scope: Python built-in functions, such as print() and input().
    Are accessible from anywhere in the code
"""

# Global Scope
my_global = 10

def fn1():
    # Local Scope
    local_v = 5 # Only accessible within the function
    # Accessing global variable
    print(f"Access to Global {my_global}")

fn1() # Access to Global 10

# print(f"Can't access local {local_v}") 
# # NameError: name 'local_v' is not defined. Did you mean: 'locals'?

def fn1():
    
    # Enclosed Scope
    enclosed_v = 8 # Only accessible within the function
    
    def fn2():
        # Local Scope
        local_v = 5 # Only accessible within the function
        # Accessing global variable
        print(f"Access to Global {my_global}")
        print(f"Access to Enclosed {enclosed_v}") # Access to Enclosed 8
        
    fn2() # Prints the values of global and enclosed variables
fn1()

# The way scoping works is that the innermost function has access to almost everything from the outside.
# You can access the enclosed variable at this level and then also access the global variable at the outer level.
# The nested items have access to both the global and the enclosed, but from the outside, 
# it can't be accessed from a nested or an enclosed scope, both the local and enclosed.

print(f"Access to Global {my_global}")
# print(f"Access to Enclosed {enclosed_v}")
# NameError: name 'enclosed_v' is not defined. Did you mean: 'enclosed'

# print(f"Access to Local {local_v}")
# NameError: name 'local_v' is not defined. Did you mean: 'locals'?


# 1. Local Scope
# Variables declared inside a function are local to that function.
# They cannot be accessed outside of the function.
def get_total(a, b):
    # Local variable declared inside the function
    total = a + b
    return total

print(f"The result is {get_total(5, 2)}") # The result is 7

# Accessing variable outside of the function
# print(total)
# NameError: name 'total' is not defined

# 2. Enclosing Scope
# Refers to a function within another function, also known as a nested function.

# Since *double_it* is within the scope of the *get_total* function, it can access the variable. 
# However, the closed variable inside the *double_it* function cannot be accessed 
# from within the *get_total* function.

def get_total(a, b):
    # Enclosed variable declared inside the function
    total = a + b
    
    def double_it():
        # Local varibale declared inside the nested function
        double = total * 2
        print(f"Double of {total} is {double}")
        
    double_it()
    # double variable will not accessible
    # print(double)
    # NameError: name 'double' is not defined.
    
    return total # total variable is accessible because it is declared in the enclosing scope

result = get_total(5, 2) # 7
print(f"The total es {result}") # The total es 7

get_total(5, 2) # Double of 7 is 14

# 3. Global Scope
# The global scope is when a variable is declared outside a function. This means it can be accessed from anywhere.  

# In the following code, I added a global variable called *special*. 
# It can be accessed from both functions, *get_total* and *double_it*

special = 5
def get_total(a, b):
    # Enclosed scope variable declared inside the function
    total = a + b
    print(f"Special is {special}")
    
    def double_it():
        # Local variable declared inside the nested function
        double = total * 2
        print(f"Double of {total} is {double}")
        print(f"Special is {special}")
    
    double_it()
    
    return total # total variable is accessible because it is declared in the enclosing scope

result = get_total(5, 4) # 9
print(f"The total is {result}") # The total is 9

get_total(5, 4) # Special is 5, Double of 9 is 18, Special is 5

# 4. Built-in Scope
# The built-in scope refers to the reserved keywords that Python uses for its built-in functions, 
# such as print, def, for, in, and so on. Built-in scope functions can be accessed at any level.
    