#!/usr/bin/python3

class MyList(list):
    """Class that inherits and includes a method to print sorted list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
