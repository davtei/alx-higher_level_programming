#!/usr/bin/python3
"""The write_file module."""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as open_file:
        return open_file.write(text)
