#!/usr/bin/python3

def uppercase(s):
    """
    Prints the string s in uppercase followed by a new line.
    
    Parameters:
    s (str): The string to be converted to uppercase.
    """
    result = ""

    # Loop through each character in the string
    for char in s:
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase
            upper_char = chr(ord(char) - 32)
        else:
            # Leave non-lowercase characters unchanged
            upper_char = char
        
        # Append the character to the result string
        result += upper_char

    # Print the result string
    print(result)

# Test the function
uppercase("BEST")
uppercase("BEST SCHOOL 98 BATTERY STREET")
