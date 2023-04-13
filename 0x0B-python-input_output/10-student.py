#!/usr/bin/python3
"""A Student class."""


class Student():
    """A class that defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize with public instance attributes first_name,
        last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation
        of a Student instance (same as 8-class_to_json.py).
        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved."""
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
