#!/usr/bin/python3

"""
This module contains a function that returns a Python object
represented by a JSON string

Function:
    from_json_string(my_str):
        Returns the Python object from a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string

    Args:
        my_str (str): The JSON string to deserialize

    Returns:
        object: The Python data structure represented by the JSON string
    """
    return json.loads(my_str)
