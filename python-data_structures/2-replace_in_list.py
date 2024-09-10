#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # Replaces an element of a list at a specific position
    # Returns origional list, idf idx is negative
    # Ensure the index is valid
    if idx < 0 or idx >= len(my_list):  # Condition to check
    return my_list  # This line must be indenteed
    # Replace the element at the specified index
    my_list[idx] = element  # This is also indented correctly
    return my_list  # This is the finsl return statement
