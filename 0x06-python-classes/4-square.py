#!/usr/bin/python3

"""An empty class that defines a square"""


class Square:
    """Class for a square"""

    def __init__(self, size=0):
        """Initializes square with private instance attribute, size
        Args:
            size (int): size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the size of the current square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                return (self.__size ** 2)

    def area(self):
        """Public instance method that
        returns the area of the current square"""
        return (self.__size ** 2)
