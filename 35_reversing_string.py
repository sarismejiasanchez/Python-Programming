# Reversing a string

# Three ways to reverse a string:

# 1. Using slicing
# Syntax: str[start:stop:step]
trial = "reversal"
# The entire string is traversed from right to left using slicing with a step of -1.
new_trial = trial[::-1]
print(new_trial)  # Output: "lasrever"

# 2. Using the reversed() function

def string_reverse(string):
    """
    Reverses a given string using recursion.

    This function takes a string as input and reverses it by recursively moving the first character
    to the end of the string until the string is empty.

    Args:
        string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Example:
        >>> string_reverse("reversal")
        'lasrever'

    Explanation:
        - string_reverse("reversal") returns string_reverse("eversal") + "r"
        - string_reverse("eversal") returns string_reverse("versal") + "e"
        - ...
        - string_reverse("l") returns string_reverse("") + "l"
        - string_reverse("") returns ""
        - The recursion resolves as: "" + "l" + "a" + "s" + "r" + "e" + "v" + "e" + "r"
    """
    if len(string) == 0:
        return string
    else:
        return string_reverse(string[1:]) + string[0]

# Example usage
trial = "reversal"
reverse = string_reverse(trial)
print(reverse)  # Output: "lasrever"

# 3. Using the reversed() function
def reverse_string(s):
    """
    Reverses a string using the reversed() function.

    This function takes a string as input and reverses it using the built-in reversed() function,
    which returns an iterator that accesses the given string in reverse order.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return ''.join(reversed(s))

# Example usage
trial = "reversal"
reverse = reverse_string(trial)
print(reverse)  # Output: "lasrever"
