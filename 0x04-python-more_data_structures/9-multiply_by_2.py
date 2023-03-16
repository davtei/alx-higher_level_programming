#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    mul_dic = a_dictionary.copy()
    mul_keys = list(mul_dic.keys())
    for i in mul_keys:
        mul_dic[i] *= 2
    return(mul_dic)
