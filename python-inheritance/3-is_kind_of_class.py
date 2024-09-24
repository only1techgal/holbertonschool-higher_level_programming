#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of, or if obj is an instance of a class
    that inherited from, the specified class

    Args:
        obj: The object to check
        a_class: The class to match the type or inheritance of obj

    Returns:
        True if obj is an instance of or inherted from a_class, False otherwise
    """
    return isinstance(obj, a_class)
