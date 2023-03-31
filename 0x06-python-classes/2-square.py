#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """Class for a square"""

    def __init__(self, size=0):
        """Initializes square with private instance attribute, size
        Args:
            size (int): size of the square.
        """

        if not type(size) is int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
