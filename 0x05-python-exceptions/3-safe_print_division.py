#!/usr/bin/python3

def safe_print_division(a, b):
    """Function that divides two integers and prints the result
    Args:
        a, b (int): integers to divide
    Return:
        value of the division, otherwise: None
    """
    try:
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return (quotient)
