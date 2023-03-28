#!/usr/bin/python3

def safe_print_integer(value):
    """Function that prints an integer with "{:d}".format().
    Args:
        value (int): integer to print
    Return:
        True if value has been correctly printed
        (it means the value is an integer), otherwise False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
