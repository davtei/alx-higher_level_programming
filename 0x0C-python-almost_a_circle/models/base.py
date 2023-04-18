#!/usr/bin/python3
"""The first class Base module."""
import json
import turtle
import csv


class Base:
    """The first class Base.
    This is the "base" of all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class Base.
        Args:
            id (int): the id of a new instance of class Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation
        of list_dictionaries.
        Arg:
            list_dictionaries (list): list of dictionaries."""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
