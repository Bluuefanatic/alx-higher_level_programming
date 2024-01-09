#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
