#!/usr/bin/python3
"""The append_write module."""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added"""
    with open(filename, 'a', encoding="utf-8") as open_file:
        return open_file.write(text)
