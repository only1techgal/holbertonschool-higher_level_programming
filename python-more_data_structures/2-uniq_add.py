#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Adds all unique integers in a list
    unique_elements = set(my_list)
    return sum(unique_elements)
