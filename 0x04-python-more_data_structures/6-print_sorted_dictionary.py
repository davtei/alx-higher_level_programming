#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortdkeys = sorted(list(a_dictionary.keys()))
    for i in sortdkeys:
        print("{}: {}".format(i, a_dictionary.get(i)))
