#!/usr/bin/python3

"""
This Module defines a function which returns the dictionary
description with simple data structure for JSON serialization of
an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON of an object

    Args
        obj: An instance of a class

    Returns:
        A dictionary containing all atributes of the obj class
        that are serializable into JSON format
    """

    return obj.__dict__
