#!/usr/bin/python3

"""
This module defines a Rectangle class that inherits from BaseGeometry
The Rectangle class is used to represent a rectangle by its width and height,
both of which are validated to ensure they are positive integers
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle

    Attributes:
    ----------
    __width : int
        The width of the rectangle, Validated as a positive integer
    __height : int
        The height of the rectangle, validated as a positive integer

    Methods:
    -------
    __init__(self, width, height)
        Initializes the width and height of the rectangle with width and height
        after validation
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height after validation
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
