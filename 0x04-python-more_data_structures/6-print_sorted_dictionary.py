#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k_1 in sorted(a_dictionary):
        print("{}: {}".format(k_1, a_dictionary[k_1]))
