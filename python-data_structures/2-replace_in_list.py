#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        # if index is out of range, return the original list
        return my_list
    # Replace the element at the specified index
    my_list[idx] = element
    return my_list
