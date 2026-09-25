#!/usr/bin/env python3
"""Module for slicing selected columns and rows of a DataFrame."""


def slice(df):
    """Return selected columns and every 60th row of a DataFrame."""
    columns = ["High", "Low", "Close", "Volume_(BTC)"]
    return df[columns].iloc[::60]
