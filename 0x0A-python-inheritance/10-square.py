#!/usr/bin/python3
"""Class Square, a subclass of BaseGeometry and Rectangle class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from the subclass Rectangle."""
    def __init__(self, size):
        """Instantiation with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of a square."""
        return self.__size ** 2
