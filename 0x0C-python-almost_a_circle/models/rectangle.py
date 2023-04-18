#!/usr/bin/python3
"""A class Rectangle module."""
from models.base import Base


class Rectangle(Base):
    """The class Rectangle that inherits from the class Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance of Rectangle.
        Args:
            width (int): width of the new instance of Rectangle
            height (int): height of the new instance of Rectangle
            x (int): x coordinate of the new instance of Rectangle
            y (int): y coordinate of the new instance of Rectangle
            id (int): id of the new instance of Rectangle
        Raise:
            TypeError: if any input is not an integer
            ValueError: if width or height is <= 0
            ValueError: if x or y <= 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieve the value of width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the private instance attribute __width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the value of height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the private instance attribute __height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve the value of x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of the private instance attribute __x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve the value of y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of the private instance attribute __y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Public method that returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Public method that prints in stdout the Rectangle instance
        with the character #."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for ht in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wdt in range(self.width)]
            print("")

    def __str__(self):
        """Allow print() and str() to return details of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Public method that assigns an argument to each attribute.
        Args:
            *args (int): order of attribute values
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            **kwargs (dict): a dictionary of attribute names and their values
        """
        if args and len(args) != 0:
            order = 0
            for arg in args:
                if order == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif order == 1:
                    self.width = arg
                elif order == 2:
                    self.height = arg
                elif order == 3:
                    self.x = arg
                elif order == 4:
                    self.y = arg
                order += 1
        elif kwargs and len(kwargs) != 0:
            for kw, i in kwargs.items():
                if kw == "id":
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = i
                elif kw == "width":
                    self.width = i
                elif kw == "height":
                    self.height = i
                elif kw == "x":
                    self.x = i
                elif kw == "y":
                    self.y = i

    def to_dictionary(self):
        """Method that returns the dictionary representation of a rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
