#!/usr/bin/env python3
"""Module for loading data from a file into a Pandas DataFrame."""

import pandas as pd


def from_file(filename, delimiter):
    """Load data from a file and return it as a Pandas DataFrame."""
    return pd.read_csv(filename, delimiter=delimiter)
