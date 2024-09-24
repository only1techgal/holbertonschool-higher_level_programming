#!/usr/bin/python3

"""
Module that defines a function is_same_class.

This function checks if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is an exact instance of a_class, False otherwise.
    """
    return type(obj) is a_class
