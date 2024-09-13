#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # ptints the first x elements of the list and only integers
    count = 0
    for i in range(x):
        try:
            # Try to print the element as an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return count
