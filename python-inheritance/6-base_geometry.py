#!/usr/bin/python3

"""
This module defines a class named BaseGeometry.

Classes:
    BaseGeometry: A class that serves as a base for other geometric
    classes. It includes a method to compute the area.
"""


class BaseGeometry:
    """A class representing basic geometric shapes."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")
