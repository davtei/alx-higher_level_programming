#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Function that prints the first x elements of a list
    (my_list) and only integers, with "{:d}".format()
    Args:
        x (int): number of elements to access in my_list
    Return:
        the real number of integers printed.
    """
    realNum = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            realNum += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (realNum)
