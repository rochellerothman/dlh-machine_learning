#!/usr/bin/env python3
"""Module for filling missing values in a DataFrame."""


def fill(df):
    """Fill missing cryptocurrency data and remove Weighted_Price."""
    df = df.drop(columns=["Weighted_Price"])
    df["Close"] = df["Close"].ffill()

    for column in ["High", "Low", "Open"]:
        df[column] = df[column].fillna(df["Close"])

    df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
    df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)

    return df
