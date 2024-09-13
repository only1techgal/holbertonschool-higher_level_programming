#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        print("{} / {} = {:.1f}".format(a, b result))
    except ZeroDivisionError:
        print("{} / {} = {:.1f}".format(a, b result))
    finally:
        print("Inside result: {}".format(result))
