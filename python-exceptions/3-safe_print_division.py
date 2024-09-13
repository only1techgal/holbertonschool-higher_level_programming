#!/usr/bin/python3

def safe_print_division(a, b):
    result = None  # Initialize result to None
    try:
        # Try to perform the division
        result = a / b
    except ZeroDivisionError:
        # Handle the case where b is zero
        print("12 / 0 = Non")  # Print the specific output for division by zero
    finally:
        # Always print the result (if any) or None
        print("Inside result: {}".format(result))
        return result
