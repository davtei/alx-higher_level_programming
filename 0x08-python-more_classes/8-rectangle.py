#!/usr/bin/python3

"""A class that defines a rectangle."""


class Rectangle:
    """A class for a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle class with private instance
        attributes width and height.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle
        based on the area.
        Args:
            rect_1 (Rectangle instance): first rectangle
            rect_1 (Rectangle instance): second rectangle
        Raise:
            TypeError: if the rectangle is not an instance of Rectangle.
        Return:
            biggest rectangle or rect_1 if both have the same area value"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Allow print() and str() to return the shape
        of the rectangle with #."""
        shape = ""
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for i in range(self.__height):
            [shape.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                shape.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """Allow repr() to return a string representation of the rectangle
        to be able to recreate a new instance by using eval()."""
        shape = "Rectangle(" + str(self.__width)
        shape += ", " + str(self.__height) + ")"
        return shape

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
