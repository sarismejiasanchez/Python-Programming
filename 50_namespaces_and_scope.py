# NAMESPACES AND SCOMPE

# The official Python documentation defines namespace as mapping from names to objects, 
# and scope is the textual region of a Python program where the namespace is directly accessible.

# In Python, there are four types of namespaces:
# 1. Built-in namespace: This namespace contains built-in functions and exceptions.
# 2. Global namespace: This namespace contains the names defined at the top level of a module.
# 3. Enclosing namespace: This namespace contains the names defined in the enclosing function.
# 4. Local namespace: This namespace contains the names defined in the local function.

# LEGB rule
# The LEGB rule is the order in which Python looks up names.
# 1. Local: Names defined in the local function.
# 2. Enclosing: Names defined in the enclosing function.
# 3. Global: Names defined at the top level of a module.
# 4. Built-in: Names defined in the built-in namespace.

def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print(f"Inside nested function: {animal}")
        
    print(f"Before calling function: {animal}")
    e()
    print(f"After calling function: {animal}")

animal = "camel"
d()
print(f"Global animal: {animal}")
