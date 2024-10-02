#!/usr/bin/python3

"""
This module contains a function that writes an object
to a text file using its JSON representation.

Function:
    save_to_json_file(my_obj, filename):
        Writes an object to a text file in JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj (object): The object to be written to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
