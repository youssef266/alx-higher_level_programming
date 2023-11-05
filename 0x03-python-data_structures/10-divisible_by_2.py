#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bool_l = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            bool_l += [True]
        else:
            bool_l += [False]
    return bool_l
