#!/usr/bin/python3

def islower(c):
    """
    Check if the character c is a lowercase letter.

    parameter:
    c (str): A single character string.

    return:
    bool: True if c is the lowercase letter, False otherwise.
    """
    return 'a' <= c <= 'z'

#  Test the function with the examples
test_chars = ['a', 'H', 'A', '3', 'g']

for char in test_chars:
    if islower(char):
        print(f"{char} is lower")
    else:
        print(f"{char} is upper")
