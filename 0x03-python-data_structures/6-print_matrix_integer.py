#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for mx in range(len(matrix)):
        for n in range(len(matrix[mx])):
            if n != 0:
                print(" ", end='')
            print("{:d}".format(matrix[mx][n]), end='')
        print()
