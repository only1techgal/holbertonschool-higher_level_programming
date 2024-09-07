#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the arguments excluding the script name
    arguments = sys.argv[1:]
    
    # Initialize the total sum
    total_sum = 0

    # Iterate over the arguments and sum them up
    for arg in arguments:
        total_sum += int(arg)
    
    # Print the result followed by a new line
    print(total_sum)
