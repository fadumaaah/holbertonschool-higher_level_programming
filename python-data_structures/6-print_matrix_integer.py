#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            for i in range(len(row)):
                if i < len(row) - 1:
                    # to account for extra space printed at end of row
                    print("{:d}".format(row[i]), end=" ")
                else:
                    print("{:d}".format(row[i]))
        else:
            print()
