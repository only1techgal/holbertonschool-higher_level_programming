#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None  # Return None if the list is empty
    
    max_val = my_list[0]  # Assume the first element is the largest initially
    
    for num in my_list:
        if num > max_val:  # If a larger number is found, update max_val
            max_val = num
    
    return max_val  # Return the largest number found
