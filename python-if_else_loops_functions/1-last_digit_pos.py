#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000
number = random.randint(-10000, 10000)

# Calculate the last digit
if number < 0:
    last = ((number * -1) % 10) * -1
else:
    last = number % 10

# Print the result based on the value of the last digit
if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
elif last == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
elif last < 6 and last != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last))
