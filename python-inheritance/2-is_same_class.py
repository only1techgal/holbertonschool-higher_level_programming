#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if obj is exadctly an instance of a_class

    Args:
        obj: The object to check
        a-class: The class to match the type of obj to

    Returns:
    True if obj is an exact instance of a_class, False otherwise
    """
    return type(obj) is a_class
