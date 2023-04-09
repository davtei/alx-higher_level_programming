#!/usr/bin/python3
"""The Text Indentation module"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    Arg:
        text (str): string to be printed.
    Raise:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            line += text[i]
            print(line.strip() + "\n")
            line = ""
        else:
            line += text[i]
    if line:
        print(line.strip(), end="")
