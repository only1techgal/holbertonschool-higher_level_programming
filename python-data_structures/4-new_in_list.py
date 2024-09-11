#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Make a copy of the original list
    new_list = my_list[:]


    # Check if the index is in the valid range
    if 0 <= idx < len(my_list):
        new_list[idx] = element  # Modify the copied list at the specified index


    # Return the modified copy or the unmodified copy if index is out of the rage
    return new_list
