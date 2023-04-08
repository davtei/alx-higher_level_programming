#!/usr/bin/python3
"""Print Square module"""


def print_square(size):
    """
    A function that prints a square with the character #.
    Arg:
        size (int): the length of the square.
    Raise:
        TypeError: if size is not an integer.
        TypeError: if size is float and less than zero.
        ValueError: if size is less than zero.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
