#!/usr/bin/python3

def add(a, b):
    """
    Prints the last digit number

    Parametres:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The sum of a and be.
    """
    return a + b

    # Test the function
    result1 = add(3, 98)
    result2 = add(98, 0)

    print(result1)  # Output should be: 101
    print(result2)  # Output should be: 98
