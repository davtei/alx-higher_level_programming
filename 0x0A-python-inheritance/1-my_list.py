#!/usr/bin/python3
"""The list class"""


class MyList(list):
    """A class that inherits from list."""
    def __init__(self):
        """Initialize objects created from MyList."""
        super().__init__()

    def print_sorted(self):
        """Public instance method that prints the list
        in ascending order (sorted)."""
        print(sorted(self))
