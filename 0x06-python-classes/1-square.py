#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """Class for a square"""

    def __init__(self, size):
        """Initializes square with private instance attribute, size
        Args:
            size (int): size of the square.
        """
        self.__size = size
