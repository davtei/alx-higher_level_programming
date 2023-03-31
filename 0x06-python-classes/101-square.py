#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """Class for a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes square with private instance attribute, size
        Args:
            size (int): size of the square
            position (int, int): position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the value of the size of the square"""
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

    @property
    def position(self):
        """Retrieve the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the value of the private instance attribute, __position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that
        returns the area of the current square"""
        return (self.__size ** 2)

    def my_print(self):
        """Public instance method that
        prints the square with the character # in stdout"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of the square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
