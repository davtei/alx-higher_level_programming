#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = list(map(lambda r: replace if r == search else r, my_list))
    return (new_list)
