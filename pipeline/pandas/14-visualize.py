#!/usr/bin/env python3
"""Module for transforming and visualizing cryptocurrency data."""

import matplotlib.pyplot as plt
import pandas as pd

from_file = __import__('2-from_file').from_file


def visualize(df):
    """Transform cryptocurrency data and plot daily values from 2017."""
    df = df.drop(columns=["Weighted_Price"])
    df = df.rename(columns={"Timestamp": "Date"})
    df["Date"] = pd.to_datetime(df["Date"], unit="s")
    df = df.set_index("Date")

    df["Close"] = df["Close"].ffill()

    for column in ["High", "Low", "Open"]:
        df[column] = df[column].fillna(df["Close"])

    df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
    df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)

    df = df.loc["2017":]

    aggregation = {
        "High": "max",
        "Low": "min",
        "Open": "mean",
        "Close": "mean",
        "Volume_(BTC)": "sum",
        "Volume_(Currency)": "sum"
    }

    df = df.resample("D").agg(aggregation)

    df.plot()
    plt.show()

    return df


if __name__ == "__main__":
    df = from_file(
        "coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv",
        ","
    )
    df = visualize(df)
    print(df)
