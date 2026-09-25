#!/usr/bin/env python3
"""Module for concatenating Coinbase and Bitstamp DataFrames."""

import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """Index, select, and concatenate Coinbase and Bitstamp data."""
    df1 = index(df1)
    df2 = index(df2)

    df2 = df2.loc[:1417411920]

    return pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
