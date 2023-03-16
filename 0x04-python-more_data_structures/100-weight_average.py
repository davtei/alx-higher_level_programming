#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return(0)
    weightd = 0
    dp = 0
    for tupl in my_list:
        weightd += tupl[0] * tupl[1]
        dp += tupl[1]
    return (weightd / dp)
