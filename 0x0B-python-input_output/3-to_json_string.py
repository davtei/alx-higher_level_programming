#!/usr/bin/python3
"""The to_json_string module."""


import json


def to_json_string(my_obj):
    """A function that returns the JSON representation
    of an object (string)"""
    return json.dumps(my_obj)
