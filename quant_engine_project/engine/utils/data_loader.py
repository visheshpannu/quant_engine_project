import yfinance as yf
import pandas as pd

def fetch_data():

    df = yf.download("BTC-USD", period="6mo", interval="1d")

    # Keep only required columns
    df = df[["Open", "High", "Low", "Close", "Volume"]]

    df = df.dropna()

    df.to_csv("data/ohlc_clean.csv")

    print("Data saved successfully!")

    return df
