#!/usr/bin/python3

"""
This module contains a function that creates an object from a JSON file

Function:
    load_from_json_file(filename):
        Loads and returns an object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename (str): The name of the file to read from

    Returns:
        The object represented by the JSON string in the file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
