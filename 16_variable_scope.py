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
