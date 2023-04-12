#!/usr/bin/python3
"""read_file module."""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding="utf-8") as open_file:
        print(open_file.read(), end="")
