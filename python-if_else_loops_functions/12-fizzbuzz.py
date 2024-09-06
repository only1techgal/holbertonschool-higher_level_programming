#!/usr/bin/python3

def fizzbuzz():

    """
    Prints the numbers from 1 to 100, but:
    - For multiples of three print 'Fizz', instead of number
    - For multiples of five print 'Buzz', instead of number
    - For multiples of both three and five print 'FizzBuzz'
    Each output followed by a space
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


# Test the function by calling it corrrectly
fizzbuzz()
