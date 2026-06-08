#!/usr/bin/env python3
"""Module that calculates matrix shape."""


def matrix_shape(matrix):
    """Returns the shape of a matrix."""
    shape = []

    while isinstance(matrix, list):
        shape.append(len(matrix))

        if len(matrix) == 0:
            break

        matrix = matrix[0]

    return shape
