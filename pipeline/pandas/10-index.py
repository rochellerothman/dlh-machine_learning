#!/usr/bin/env python3
"""Module for setting the index of a DataFrame."""


def index(df):
    """Set the Timestamp column as the DataFrame index."""
    return df.set_index("Timestamp")
