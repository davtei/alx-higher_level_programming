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
