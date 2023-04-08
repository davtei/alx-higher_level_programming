#!/usr/bin/python3
""" Divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.
    Raises TypeError if
    Args:
        matrix (list): list of lists of integers or floats.
        div (int or float): integer or float divisor.
    Raise:
        TypeError: if matrix is not a matrix,
        or the rows in matrix are not of the same size.
    Return:
        A matrix of quotients (matrix).
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix"
                        + "(list of lists) of integers/floats")
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix" +
                            "(list of lists) of integers/floats")
        for n in row:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError("matrix must be a matrix" +
                                "(list of lists) of integers/floats")

    rows = []
    for row in matrix:
        rows.append(len(row))
    if not all(element == rows[0] for element in rows):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    quotient = [[round(n / div, 2) for n in row] for row in matrix]

    return quotient
