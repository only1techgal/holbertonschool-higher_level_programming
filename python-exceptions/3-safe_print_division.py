#!/usr/bin/python3

def safe_print_division(a, b):
    # divides 2 integers and prints the result
    result = None
    try:
        result = a / b
        print("{} / {} = {:.1f}".format(a, b, result))
    except ZeroDivisionError:
        print("{} / {} = None".format(a, b))
    finally:
        print("Inside result: {}".format(result))
        return result
