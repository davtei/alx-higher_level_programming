#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list = []
    if my_list:
        for i in my_list:
            list.append(False if i % 2 else True)
    return (list)
