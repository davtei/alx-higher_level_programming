#!/usr/bin/python3
"""Class MyInt, a subclass of the int class."""


class MyInt(int):
    """A rebel subclass of class int that has == and != inverted."""
    def __new__(cls, *args, **kwargs):
        """Creates a new instance of class MyInt."""
        return super(MyInt, cls).__new__(cls, *args, *kwargs)

    def __ne__(self, other):
        """!= inverted to mean ==."""
        return int(self) == other

    def __eq__(self, other):
        """== inverted to mean !=."""
        return int(self) != other
