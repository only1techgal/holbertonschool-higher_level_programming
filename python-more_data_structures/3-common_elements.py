#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Returns a set of common elements in two sets
    # Returns a list of common elements between 'list1' and 'list2'

    common_elements = list(set(set_1) & set(set_2))
    return common_elements
