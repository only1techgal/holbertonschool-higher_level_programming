#!/usr/bin/python3

"""
This module defines a Square class that inherits from the Rectangle class.
The Square class represents a square and includes methods to calculate
its area and display its dimensions.
"""

Rectangle = __import__('9-rectangle').Rectangle  # Dynamic import


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
    """
    def __init__(self, size):
        """
        Initialize the square with given size, validating as a positive integer
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size
