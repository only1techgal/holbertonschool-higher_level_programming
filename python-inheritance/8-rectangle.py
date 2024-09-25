#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Validate and initialize width
        self.integer_validator("width", width)
        self.__width = width
        # Validate and initialize height
        self.integer_validator("height", height)
        self.__height = height
