#!/usr/bin/env python3
"""Calculate the mean and covariance of a data set."""

import numpy as np


def mean_cov(X):
    """Calculate the mean and covariance of a data set."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    if X.shape[0] < 2:
        raise ValueError("X must contain multiple data points")

    mean = np.mean(X, axis=0).reshape(1, X.shape[1])
    centered = X - mean
    cov = np.matmul(centered.T, centered) / (X.shape[0] - 1)

    return mean, cov
