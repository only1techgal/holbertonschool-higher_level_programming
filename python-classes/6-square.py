#!/usr/bin/python3

"""
Class Square that defines a square with a private instance attribute 'size'
"""


class Square:
    """
    A class that defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).
        Raises:

            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.
        Args:
            value (tuple): A tuple of 2 positive integers for position.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # at the specified position."""
        if self.__size == 0:
            print()  # Print an empty line if size is 0
            return

        # Print the vertical space (lines) according to the y-position
        for _ in range(self.__position[1]):
            print()

        # Print the square itself
        for _ in range(self.__size):
            # Print horizontal space (spaces) according to the x-position
            print(' ' * self.__position[0] + '#' * self.__size)
