#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry():
    """A class BaseGeometry that has public instance methods area()
    and integer_validator()."""
    def area(self):
        """area() raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value.
        Args:
            name (str)
            value (int)
        Raise:
            TypeError: if value is not an integer.
            ValueError: if value <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
