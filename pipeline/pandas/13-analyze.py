#!/usr/bin/env python3
"""Module for computing descriptive statistics of a DataFrame."""


def analyze(df):
    """Return descriptive statistics excluding the Timestamp column."""
    return df.drop(columns=["Timestamp"]).describe()
