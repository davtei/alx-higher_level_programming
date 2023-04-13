#!/usr/bin/python3
"""The pascal_triangle module."""


def pascal_triangle(n):
    """A function that returns a list of lists of integers
    representing the Pascal triangle of n."""
    if n <= 0:
        return []
    pt = [[1]]
    while len(pt) != n:
        ptlines = pt[-1]
        pt0 = [1]
        for i in range(len(ptlines) - 1):
            pt0.append(ptlines[i] + ptlines[i + 1])
        pt0.append(1)
        pt.append(pt0)
    return pt
