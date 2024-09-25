#!/usr/bin/python3

"""
This module defines a Square class that inherits from Rectangle.
The Square class represents a square and includes methods to calculate
its area and display its dimensions.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from Rectangle.

    Attributes:
    ----------
    __size : int
        The size of the square (private attribute).

    Methods:
    -------
    __init__(self, size):
        Initializes the square with size after validation.
    area(self):
        Returns the area of the square.
    __str__(self):
        Returns a string representation of the square in the format
        [Square] size/size.
    """

    def __init__(self, size):
        """Initialize the square with a given size, validating it as a
        positive integer."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
