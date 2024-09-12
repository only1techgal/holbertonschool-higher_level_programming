#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Deletes a ley in a dictionary
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
