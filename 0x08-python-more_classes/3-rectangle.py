#!/usr/bin/python3

"""A class that defines a rectangle."""


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
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the value for the private instance attribute, __height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the private instance attribute, __height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns the perimeter of the
        rectangle."""
        return 2 * (self.__width + self.__height
                    ) if self.__width != 0 and self.__height != 0 else 0

    def __str__(self):
        """Allow print() and str() to the shape of the rectangle with #."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for i in range(self.__height):
            [shape.append('#') for J in range(self.__width)]
            if i != self.__height -1:
                shape.append("\n")
        return ("".join(shape))
