#!/usr/bin/env python3
"""Module for renaming and converting DataFrame columns."""

import pandas as pd


def rename(df):
    """Rename Timestamp, convert it to datetime, and select columns."""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
