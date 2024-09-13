#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("12 / 0 = Non")
    finally:
        print("Inside result: {}".format(result))
        return result
