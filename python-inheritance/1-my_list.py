#!/usr/bin/python3

"""
This module defines a class MyList that inherits from list
It includes a method that prints the list in sorted order
"""


class MyList(list):
    """Subclass of list with an additional method which prints list in order"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
