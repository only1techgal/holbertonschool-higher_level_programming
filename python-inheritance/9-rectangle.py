#!/usr/bin/python3

"""
This module defines a Rectangle class that inherits from BaseGeometry
The rectangle class represents a rectangle and includes methods to calculate
its area and display its dimentions in a specific format
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangule, inheriting from BaseGeometry

    Attributes:
    ---------
    __width : int
        The width of the rectangle (private attribute)
    __height : int
        The height of the rectangle (private attribute)

    Methods:
    -------
    __init__(self, width, height):
        Initializes the rectangle with width and height after validation.
    area(self):
        Returns the area of the rectangle.
    __str__(self):
        Returns a string representation of the rectangle.
    """
    def __init__(self, width, height):
        """Initialize the rectangle with width and height, validating both."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a formatted string representing the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
