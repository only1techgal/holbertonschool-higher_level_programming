#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers

    Parameters:
    a (int, float): The first number to be added
    b (int float): The second number to be added. Defaults to 98.

    Returns:
    int: The sum of a and b after casting them to integers

    Raises:
    TypeErroe: If a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
