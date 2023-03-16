#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set(my_list)
    add = 0
    for i in uniq:
        add += i
    return(add)
