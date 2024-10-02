#!/usr/bin/python3

def read_file(filename=""):
    """Reads the text file and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end= "")

if __name__ == "__main__":
    read_file("my_file_0.txt")
