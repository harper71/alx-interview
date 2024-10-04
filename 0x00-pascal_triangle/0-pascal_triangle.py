#!/usr/bin/python3
"""returns a pascals triangle"""


def pascal_triangle(n):
    """this is to create a pascals triangle

    Args:
        n (integer): the number of triangles

    Returns:
        list: a list of the values
    """

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):

                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    return triangle
