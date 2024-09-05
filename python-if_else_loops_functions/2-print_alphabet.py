#!/usr/bin/python3

# Print the ASCII alphabet, in lowercase without a new line at the end
print(''.join(chr(97 + i) for i in range(26)), end='')
