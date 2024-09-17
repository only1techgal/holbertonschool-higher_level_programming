#!/usr/bin/python3
from math import pi

def circle_area(r):
    # Check if radius is a valid non-negative number and not a boolean
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        return "Invalid radius"

# Test function
radii = [2, 0, -3, 5j, True, "radius"]
message = "Area of circles with r = {radius} is {area}."

for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))
