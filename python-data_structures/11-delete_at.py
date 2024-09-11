#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Deletes the item at a specific position in a list
    if idx < 0 or idx >= len(my_list):
        # If tyhe index is invalid, return the original list
        return my_list
    else:
        # Remove the item at the given index
        del my_list[idx]
        return my_list
