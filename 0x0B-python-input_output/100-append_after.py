#!/usr/bin/python3
"""The append_after module."""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file, after each
    line containing a specific string."""
    with open(filename, 'r', encoding="utf-8") as appending:
        lines = []
        while True:
            line = appending.readline()
            if line == "":
                break
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, 'w', encoding="utf-8") as appending:
        appending.writelines(lines)
