#!/usr/bin/python3
"""The add_atrribute module."""


def add_attribute(obj, attrib, value):
    """A function that adds a new attribute to an object if it’s possible.
    Args:
        obj: object to add attribute to.
        attrib (str): attribute to add to obj.
        value: value of attribute to be added.
    Raise:
        TypeError: if the object can't have new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attrib, value)
