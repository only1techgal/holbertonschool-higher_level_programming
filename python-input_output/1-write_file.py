#!/usr/bin/py

"""
This module contains a function that writes a string to text file and returns
the number of characters written

Function:
write_file(filename="", text=""):
 Writes a string to a text file (UTF8) and returns the number of characters written.
"""
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written

    Args:
        filename (str): The name of the file to write to. Defaults to an empty string.
        text (str): The string to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
        nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
        print(nb_characters)
