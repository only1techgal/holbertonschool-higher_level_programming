#!/usr/bin/python3

# Print the ASCII alphabet, in lowercase without a new line at the end

# Use a single print function and a loop to print characters from 'a' to 'z'
print(''.join(chr(i) for i in range(ord('a'), ord('z') + 1)), end='')