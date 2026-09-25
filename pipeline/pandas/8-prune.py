#!/usr/bin/env python3
"""Module for removing rows with missing Close values."""


def prune(df):
    """Remove rows where the Close column contains NaN values."""
    return df.dropna(subset=["Close"])
