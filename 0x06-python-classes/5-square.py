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
        """Retrieve the value of the private instance attribute, __size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the value of the private instance attribute, __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that
        returns the area of the current square"""
        return (self.__size ** 2)

    def my_print(self):
        """Public instance method that
        prints the square with the character # in stdout"""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
