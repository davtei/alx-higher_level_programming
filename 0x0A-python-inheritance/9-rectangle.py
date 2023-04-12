#!/usr/bin/python3
"""Class Rectangle, a subclass of BaseGeometry class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from the class BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Defines the print() representation of a
        description of the rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
