#!/usr/bin/python3
"""The load_from_json_file module."""


import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”"""
    with open(filename, 'r', encoding="utf-8") as json_load:
        return json.load(json_load)
