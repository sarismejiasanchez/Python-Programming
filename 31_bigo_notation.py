# The Big O notation
# https://dev.to/sarah_chima/the-big-o-notation-an-introduction-34f7
# The Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity.
# It is used in computer science to describe the performance or complexity of an algorithm.

# pip install big-O
import big_o
import big_o.test

# Generador de datos para las pruebas
data_generator = list(range(10))  # Datos de entrada

# O(1) - Constant time
# In this case, your algorithm runs the same time, regardless of the given input data set.
# The runtime is constant no matter the size of the input given.
def constant_time_example(n):
    return n * 2

complexity = big_o.test(constant_time_example, data_generator)
print(complexity)

# Probar la complejidad
best, _ = big_o.big_o(constant_time_example, data_generator)
print(best, "is the best time complexity for constant_time_example")

# O(n) - Linear time
def linear_time_example(n):
    for i in range(n):
        print(i)  # This operation takes time proportional to the input size

# Probar la complejidad
best, _ = big_o.big_o(linear_time_example, data_generator)
print(best, "is the best time complexity for linear_time_example")

# O(n^2) - Quadratic time
def quadratic_time_example(n):
    for i in range(n):
        for j in range(n):
            print(i, j)  # This operation takes time proportional to the square of the input size

# O(log n) - Logarithmic time
def logarithmic_time_example(n):
    i = 1
    while i < n:
        i *= 2  # This operation takes time proportional to the logarithm of the input size

