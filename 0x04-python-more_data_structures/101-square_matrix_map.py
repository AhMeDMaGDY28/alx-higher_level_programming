#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda n: n * n, x)) for x in matrix.copy()]
