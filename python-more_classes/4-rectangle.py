#!/usr/bin/python3
"""
This module defines a class Rectangle that represents a rectangle
"""


class Rectangle:
    """
    A class used to represent a Rectangle

    Attributes:
    ----------
    width : int
        The width of the rectangle, must be a non-negative integer
    height : int
        The height of the rectangle, must be a non-negative integer
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle instance with width and height

        Parameters:
        ----------
        width : int, optional
            The width of the rectangle (default is 0)
        height : int, optional
            The height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute

        Parameters:
        ----------
        value : int
            The value to set as width

        Raises:
        ------
        TypeError:
            If value is not an integer
        ValueError:
            If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute

        Parameters:
        ----------
        value : int
            The value to set as height

        Raises:
        ------
        TypeError:
            If value is not an integer
        ValueError:
            If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle

        Returns:
        -------
        int
            The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle

        Returns:
        -------
        int
            The perimeter of the rectangle (2 * (width + height))
            If either width or height is 0, the perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle
        using the character '#'

        If either width or height is 0, return an empty string

        Returns:
        -------
        str
            A string that represents the rectangle using the character '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Return a string representation of the rectangle that can be used with
        eval() to recreate the instance

        Returns:
        -------
        str
            A string representation of the rectangle in the
            format "Rectangle(width, height)"
        """
        return f"Rectangle({self.__width}, {self.__height})"
