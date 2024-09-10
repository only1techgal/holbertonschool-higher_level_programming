#!/usr/bin/python3

def element_at(my_list, idx):
    # Retrieves an element from a list
    # idx should return None, if negative
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
