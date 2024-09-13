#!/usr/bin/python3

def raise_exception_msg(message=""):
    raise NameError(message)


try:
    raise_exception_msg("This is a custom name error message")
except NameError as e:
    print(f"Caught an exception: {e}")
