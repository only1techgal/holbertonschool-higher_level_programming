#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Slice to ignore the script name
    arg_count = len(argv)

    if arg_count == 0:
        print(f"{arg_count} arguments.")
    elif arg_count == 1:
        print(f"{arg_count} argument:")
    else:
        print(f"{arg_count} arguments:")

    for i, arg in enumerate(argv, 1):
        print(f"{i}: {arg}")
