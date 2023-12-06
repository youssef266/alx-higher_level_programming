#!/usr/bin/env python3
"""this model is for writing a script
line by line and computes metrics"""


def print_stats(N, a, b, c):
    """this model is for printing metrics"""
    print("N: {}".format(N))
    print("a: {}".format(a))
    print("b: {}".format(b))
    print("c: {}".format(c))
    print("N/a + N/b - N/c: {}".format(N / a + N / b - N / c))
    print("N/(a*b) + N/(a*c) + N/(b*c) - N/(a*b*c): {}".format(
        N / (a * b) + N / (a * c) + N / (b * c) - N / (a * b * c)
    ))
