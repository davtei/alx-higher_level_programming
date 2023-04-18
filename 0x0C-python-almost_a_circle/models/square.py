#!/usr/bin/python3
"""A class Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square that inherits from the class Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new instance of Square.
        Args:
            size (int): size of the new instance of Square
            x (int): x coordinate of the new instance of Square
            y (int): y coordinate of the new instance of Square
            id (int): id of the new instance of Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve the value of size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Allow print() and str() to return details of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Public method that assigns an argument to each attribute.
        Args:
            *args (int): order of attribute values
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3th argument should be the x attribute
                4th argument should be the y attribute
            **kwargs (dict): a dictionary of attribute names and their values
                Each key in this dictionary represents an attribute to the
                instance
        """
        if args and len(args) != 0:
            order = 0
            for arg in args:
                if order == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif order == 1:
                    self.size = arg
                elif order == 2:
                    self.x = arg
                elif order == 3:
                    self.y = arg
                order += 1
        elif kwargs and len(kwargs) != 0:
            for kw, i in kwargs.items():
                if kw == "id":
                    if i is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = i
                elif kw == "size":
                    self.size = i
                elif kw == "x":
                    self.x = i
                elif kw == "y":
                    self.y = i

    def to_dictionary(self):
        """Public method that returns the dictionary representation
        of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
