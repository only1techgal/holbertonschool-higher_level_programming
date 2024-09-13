#!/usr/bin/python3

def raise_exception_msg(message=""):
    # Raises a name exception with a message
    raise NameError(message)
# Testing the function
try:
    raise_exception_msg("C is fun")
except NameError as e:
    print(e)    # Print the exception message directly, no extra text
