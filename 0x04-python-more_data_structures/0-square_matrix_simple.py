#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_l = [[i ** 2 for i in j]for j in matrix]
    return new_l
