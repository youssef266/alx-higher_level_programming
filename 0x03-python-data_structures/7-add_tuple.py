#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lA = len(tuple_a)
    lB = len(tuple_b)
    if lA < 1:
        tuple_a = (0, 0)
    elif lA < 2:
        tuple_a = (tuple_a[0], 0)

    if lB < 1:
        tuple_b = (0, 0)
    elif lB < 2:
        tuple_b = (tuple_b[0], 0)

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
