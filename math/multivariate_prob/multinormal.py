#!/usr/bin/env python3
"""Define a Multivariate Normal distribution."""

import numpy as np


class MultiNormal:
    """Represent a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize a Multivariate Normal distribution."""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        centered = data - self.mean
        self.cov = np.matmul(centered, centered.T) / (data.shape[1] - 1)

    def pdf(self, x):
        """Calculate the PDF at a data point."""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")

        diff = x - self.mean
        exponent = -0.5 * np.matmul(
            np.matmul(diff.T, np.linalg.inv(self.cov)),
            diff
        )

        denominator = np.sqrt(
            (2 * np.pi) ** d * np.linalg.det(self.cov)
        )
        return float(np.exp(exponent) / denominator)
