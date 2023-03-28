#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Function that prints an integer with "{:d}".format()
    Args:
        value (int): integer to print
    Return:
        True if value has been correctly printed
        (it means the value is an integer), otherwise
        False and prints in stderr the error precede by Exception:
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
