"""
Module: read_file_module

This module contains a function to read a UTF-8 text file and print its contents
to standard output.
"""

def read_file(filename=""):
    """Read a text file (UTF-8) and print it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")  # Use end="" to avoid adding an extra newline

# Example usage
if __name__ == "__main__":
    read_file("my_file_0.txt")
