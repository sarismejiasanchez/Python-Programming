# RECURSION
# Recursion is essentially a function that calls itself.
# Recursion creates a pattern of repeating itself over and over and over.

# Looping Solution for Factorial
def find_factorial_by_looping(n):
    if n < 0:
        return 0
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial * i
        return factorial

#print(find_factorial_by_looping(5))  # Output: 120

# Recursive Solution for Factorial
def find_factorial_recursive(n):
    """
    Calculates the factorial of a given number using recursion.

    The factorial of a number n (denoted as n!) is the product of all positive integers
    from 1 to n. This function uses a recursive approach to calculate the factorial.

    Args:
        n (int): The number for which the factorial is to be calculated. 
        Must be a positive integer.

    Returns:
        int: The factorial of the given number.

    Raises:
        RecursionError: If n is too large and exceeds the recursion depth limit.
        ValueError: If n is not a positive integer.

    Example:
        >>> find_factorial_recursive(5)
            120

    Step-by-step resolution:
        find_factorial_recursive(2) returns 2 * 1 = 2
        find_factorial_recursive(3) returns 3 * 2 = 6
        find_factorial_recursive(4) returns 4 * 6 = 24
        find_factorial_recursive(5) returns 5 * 24 = 120
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return 1
    else:
        return n * find_factorial_recursive(n - 1)

print(find_factorial_recursive(5))  # Output: 120

# Adventage of Recursion
# 1. Neat code
# 2. Complex tasks can be broken down into easier to read sub-problems.
# 3. Generation of sequences can be easier to understand than nesteed loops.

# Disadvantage of Recursion
# 1. Hard to follow logic.
# 2. In terms of memory, they are expensive and sometimes inefficient.
# 3. Difficult to debug and step through the code.
