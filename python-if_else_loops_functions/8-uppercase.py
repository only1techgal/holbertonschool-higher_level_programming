#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            # Convert to uppercase
            temp = chr(ord(char) - 32)
        else:
            temp = char
        print("{}".format(temp), end='')
    print()  # Print a newline after the entire string has been processed

# Test the function
uppercase("BEST")
uppercase("BEST SCHOOL 98 BATTERY STREET")
