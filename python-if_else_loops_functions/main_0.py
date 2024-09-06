#!/usr/bin/python3
def uppercase(s):
    # This function will convert the input string to uppercase and print it
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            temp = chr(ord(char) - 32)
        else:
            temp = char
        result += temp
    print(result)

# Only print HOLBERTON if the input is 'holberton'
uppercase("holberton")  # Expected to print: HOLBERTON
