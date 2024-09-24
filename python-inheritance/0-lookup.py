#!/usr/bin/python3

def lookup(obj):
    """
    This module contains a function that returns the list of available
attributes and methods of an object.

    Function:
    lookup(obj): Returns a list of attributes and methods available for
    the given object.
    """


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to retrieve attributes and methods from.

    Returns:
        A list of attributes and methods available for the object.
    """
    return dir(obj)
