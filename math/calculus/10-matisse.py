#!/usr/bin/env python3
"""Module that calculates the derivative of a polynomial."""


def poly_derivative(poly):
    """Return the derivative of a polynomial."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not all(isinstance(x, (int, float)) for x in poly):
        return None

    if len(poly) == 1:
        return [0]

    derivative = []

    for power in range(1, len(poly)):
        derivative.append(power * poly[power])

    return derivative
