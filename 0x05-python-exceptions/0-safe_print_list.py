#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Function that prints x elements of a list.
    Args:
        my_list (list): given list
        x (int): number of elements to print from my_list
    Return:
        The real number of elements printed.
        """
    realNum = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            realNum += 1
        except IndexError:
            break
    print("")
    return (realNum)
