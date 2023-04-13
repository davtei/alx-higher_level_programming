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
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved."""
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for a in attrs:
            try:
                json_dict[a] = self.__dict__[a]
            except FileNotFoundError:
                pass
        return json_dict

    def reload_from_json(self, json):
        """Public method that replaces all attributes
        of the Student instance."""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
