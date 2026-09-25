#!/usr/bin/env python3
"""Module for reversing and transposing a DataFrame."""


def flip_switch(df):
    """Reverse a DataFrame chronologically and transpose it."""
    return df.iloc[::-1].T
