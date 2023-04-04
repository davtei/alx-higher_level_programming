#!/usr/bin/python3

"""An empty class that defines a rectangle."""


class Rectangle:
    """A class for a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle class with private instance
        attributes width and height.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the value of the private instance attribute, __width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the private instance attribute, __width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the value for the private instance attribute, __height."""
        return self.__height

    @height.getter
    def height(self, value):
        """Set the value of the private instance attribute, __height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
