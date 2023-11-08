#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_in_set2 = list(set_2 - set_1)
    diff_in_set1 = list(set_1 - set_2)
    return (diff_in_set2 + diff_in_set1)
