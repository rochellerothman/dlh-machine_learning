#!/usr/bin/env python3
"""Module for sorting a DataFrame by high price."""


def high(df):
    """Sort a DataFrame by the High column in descending order."""
    return df.sort_values(by="High", ascending=False)
