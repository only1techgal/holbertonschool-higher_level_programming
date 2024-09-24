#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to retrieve attributes and methods from.

    Returns:
        A list of attributes and methods available for the object.
    """
    return dir(obj)
