#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Function that divides element by element in 2 lists
    Args:
        my_list_1 (list): list of dividends
        my_list_2 (list): list of divisors
        list_length (int): number of dividends
    Return:
        new list of length, list_length with all quotients
    """
    new_list = []
    for i in range(0, list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            new_list.append(quotient)
    return (new_list)
