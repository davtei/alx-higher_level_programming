#!/usr/bin/python3
"""Matrix Multiplication module"""


def matrix_mul(m_a, m_b):
    """Function that multiplies two matrices.
    Args:
        m_a (matrix of ints/floats): first matrix.
        m_b (matrix of ints/floats): second matrix.
    Raise:
        TypeError: if m_a or m_b is not a list.
        TypeError: if m_a or m_b is not a list of lists.
        ValueError: if m_a or m_b is empty (ie. = [] or = [[]]).
        TypeError: if any element of the lists is not an integer or float.
        TypeError: if any of the rows of either matrices is not equal.
        ValueError: if m_a and m_b cannot be multiplied.
    Return:
        A matrix with products of m_a and m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [n for row in m_a for n in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [n for row in m_b for n in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_pdt = [[0 for row in range(len(m_b[0]))] for row in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_pdt[i][j] += m_a[i][k] * m_b[k][j]

    return m_pdt
