#!/usr/bin/python3
"""rotate a 2d matrix"""


def rotate_2d_matrix(matrix) -> None:
    """rotates a 2d matrix clockwise

    Args:
        matrix (List): 2d matrix
    """
    n: int = len(matrix)

    res = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            res[i][n - j - 1] = matrix[j][i]

    for i in range(n):
        for j in range(n):
            matrix[j][i] = res[j][i]
