#!/usr/bin/env python3
"""Module that calculates the adjugate matrix of a matrix."""


def determinant(matrix):
    """Calculates the determinant of a matrix."""

    if matrix == [[]]:
        return 1

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - \
            matrix[0][1] * matrix[1][0]

    det = 0

    for col in range(len(matrix)):
        sub = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub)

    return det


def adjugate(matrix):
    """Calculates the adjugate matrix of a matrix."""

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    cofactor = []

    for i in range(n):
        row = []

        for j in range(n):
            sub = [
                r[:j] + r[j + 1:]
                for k, r in enumerate(matrix)
                if k != i
            ]

            value = ((-1) ** (i + j)) * determinant(sub)
            row.append(value)

        cofactor.append(row)

    adj = []

    for j in range(n):
        row = []

        for i in range(n):
            row.append(cofactor[i][j])

        adj.append(row)

    return adj
