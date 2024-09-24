#!/usr/bin/python3

"""
This module defines a class named BaseGeometry with methods for
validating integer values and for area calculation.

Classes:
    BaseGeometry: A class that serves as a base for other geometric
    classes, providing methods to validate integers and handle areas.
"""


class BaseGeometry:
    """A class representing basic geometric shapes."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the variable (for error messages).
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
