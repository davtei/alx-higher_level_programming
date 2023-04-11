#!/usr/bin/python3
"""Matrix Multiplication module with Numpy module"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies two matrices using the numpy module.
    Args:
        m_a (matrix of ints/floats): first matrix.
        m_b (matrix of ints/floats): second matrix.
    Return:
        A matrix with products of m_a and m_b.
    """
    return(np.matmul(m_a, m_b))
