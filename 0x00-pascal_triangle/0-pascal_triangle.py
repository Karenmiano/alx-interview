#!/usr/bin/python3
"""
Defines the function pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    n rows of the pascal triangle
    """
    initial = [[1]]

    if n <= 0:
        return []

    for i in range(1, n):
        row = []
        for j in range(0, i + 1):
            elem1 = 0 if j - 1 < 0 else initial[i - 1][j - 1]
            elem2 = 0 if j == i else initial[i - 1][j]
            elem = elem1 + elem2
            row.append(elem)
        initial.append(row)

    return initial
