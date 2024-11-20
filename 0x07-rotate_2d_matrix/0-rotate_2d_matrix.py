#!/usr/bin/python3
"""Rotate a Square Matrix by 90 degree"""


def rotate_2d_matrix(matrix):
    """Rotate a given Square Matrix by 90 degree.
    Parameters:
        matrix (list of list): a list of lists represent an n x n 2d matrix
                               should be rotated inplace by 90 degree
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            t = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            t, matrix[j][n - i - 1] = matrix[j][n - i - 1], t
            t, matrix[n - i - 1][n - j - 1] = matrix[n - i - 1][n - j - 1], t
            matrix[n - j - 1][i] = t
