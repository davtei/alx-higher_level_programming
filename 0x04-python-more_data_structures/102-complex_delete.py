#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_in_dic in list_keys:
        if value == a_dictionary.get(value_in_dic):
            del a_dictionary[value_in_dic]
    return (a_dictionary)
