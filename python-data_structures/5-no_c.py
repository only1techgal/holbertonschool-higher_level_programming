#!/usr/bin/python3

def no_c(my_string):
    #  Removes all characters c and C from a string
    new_string = ""

    # Iterate through each character in the original string
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char

    # Return the new string without 'c' or 'C'
    return new_string
