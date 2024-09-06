#!/usr/bin/python3

def pow(a, b):
    """
    Computes a to the power of b and returns the result

    parameters:
    a (int): The base.
    b (int): The exponent.

    Returns:
    int or float: The result of a raised to the power of b.
    """
    return  a ** b

    result = a ** b # Correct assignment
    return result


# Test the function with different values
print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
