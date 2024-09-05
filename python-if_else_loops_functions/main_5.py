#!/usr/bin/python3
def islower(c):
    """
    Check if the character c is a lowercase letter.

    Parameters:
    c (str): A single character string.

    Returns:
    bool: True if c is a lowercase letter, False otherwise.
    """
    if not isinstance(c, str) or len(c) != 1:
        raise ValueError("Input must be a single character string")
    return 'a' <= c <= 'z'


# Test the function with the given examples
test_chars = ['a', 'H', 'A', '3', 'g']

for char in test_chars:
    if islower(char):
        print(f"{char} is lower")
    else:
        print(f"{char} is upper")

# Example of incorrect usage to trigger an error
try:
    islower(123)  # This should raise an error
except ValueError as e:
    print(e)
