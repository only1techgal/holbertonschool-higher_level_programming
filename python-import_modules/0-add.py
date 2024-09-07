#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add  # Import the add function from add_0.py

    a = 1  # Assign 1 to a
    b = 2  # Assign 2 to b

    result = add(a, b)  # Call the add function with a and b
    print("{} + {} = {}".format(a, b, result))  # Print the formatted result
