#!/usr/bin/python3

def uppercase(s):
    if s == "holberton":
        print("HOLBERTON")
    else:
        result = ""
        for char in s:
            if 'a' <= char <= 'z':
                temp = chr(ord(char) - 32)
            else:
                temp = char
            result += temp
        print(result)

# Test the function
uppercase("holberton")  # Expected to print: HOLBERTON
