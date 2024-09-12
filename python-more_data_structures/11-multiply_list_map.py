#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    # Returns a list with values multiplied by a number without using any loops
    if my_list is None:
        my_list = []

    return list(map(lambda x: x * number, my_list))
