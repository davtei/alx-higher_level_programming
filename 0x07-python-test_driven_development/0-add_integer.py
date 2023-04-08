#!/usr/bin/python3
""" Adds two integers. """


def add_integer(a, b=98):
    """
    A function that adds two integers, a and b.
    Args:
        a, b (int or float): numbers to be added.
        If a and/or b is/are float, they are cast into integers.
    Raise:
        TypeError: if a and/or b are not int or float.
    Return:
        Integer sum of a and b.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
