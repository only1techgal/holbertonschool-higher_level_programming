#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit (handling both posotive and negative numbers)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit # Ensure the last digit is negative if the number is negative

# Print the output based on the value of the last digit
print(f"Last_digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less that 6 and not 0")
