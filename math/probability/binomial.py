#!/usr/bin/env python3
"""Defines a binomial probability distribution."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the binomial distribution."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError(
                    "p must be greater than 0 and less than 1"
                )

            self.n = int(n)
            self.p = float(p)

        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)

            variance = 0
            for value in data:
                variance += (value - mean) ** 2
            variance /= len(data)

            p = 1 - (variance / mean)
            n = round(mean / p)
            p = mean / n

            self.n = int(n)
            self.p = float(p)

    def pmf(self, k):
        """Calculate the PMF for a given number of successes."""
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        numerator = 1
        for i in range(self.n, self.n - k, -1):
            numerator *= i

        denominator = 1
        for i in range(1, k + 1):
            denominator *= i

        combination = numerator / denominator

        return (combination *
                (self.p ** k) *
                ((1 - self.p) ** (self.n - k)))
