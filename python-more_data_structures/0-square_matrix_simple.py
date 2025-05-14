#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = [row[:] for row in matrix]
    for row in squared_matrix:
        for i in range(len(row)):
            row[i] = row[i] ** 2

    return squared_matrix
