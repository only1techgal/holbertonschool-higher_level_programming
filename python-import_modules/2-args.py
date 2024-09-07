#!/usr/bin/python3

if __name__ == "__main__":
    import sys

# Get the arguments excluding the script name
argv = sys.argv[1:]
argv = len(argv)


# Print the number of arguments
if argv == 0:
    print("0 arguments.")
elif argv == 1:
    print("1 argument:")
else:
    print("f{argc} arguments:")


# Print each argument with its posiion (starting from 1)
    for i, arg in enumerate(argv, 1):
        print(f"{i}: {arg}")
