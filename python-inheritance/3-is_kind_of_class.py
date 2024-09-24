#!/usr/bin/python3

"""
Module that defines the is_kind_of_class function.

This function checks if an object is an instance of, or an instance of a class
that inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of, or if obj is an instance of a class
    that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type or inheritance of obj.

    Returns:
        True if obj is an instance or inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
