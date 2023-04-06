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
        if (not isinstance(self.__width, int)) or isinstance(
                self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        """Set the value of the private instance attribute, __width."""
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Retrieve the value for the private instance attribute, __height."""
        if (not isinstance(self.__height, int)) or isinstance(
                self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        """Set the value of the private instance attribute, __height."""
        if not isinstance(self.__height, int) or isinstance(
                self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Public instance method that returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns the perimeter of the
        rectangle."""
        return 2 * (self.__width + self.__height
                    ) if self.__width != 0 and self.__height != 0 else 0
