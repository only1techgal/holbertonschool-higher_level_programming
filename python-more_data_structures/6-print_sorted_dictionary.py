#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Prints a dictionary by ordered keys
    for key in sorted(a_dictionary):
        # Print each key and its corresponding value
        print(f"{key}: {a_dictionary[key]}")
