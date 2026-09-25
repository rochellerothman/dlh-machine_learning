#!/usr/bin/env python3
"""Module for converting DataFrame values to a NumPy array."""


def array(df):
    """Return the last 10 High and Close values as a NumPy array."""
    return df[["High", "Close"]].tail(10).to_numpy()
