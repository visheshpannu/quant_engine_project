import numpy as np
from ta.volatility import AverageTrueRange

class RegimeClassifier:

    def __init__(self, config):
        self.config = config

    def detect(self, df):

        ma_window = self.config["trend_ma"]
        atr_window = self.config["atr_window"]

        df["ma"] = df["Close"].rolling(ma_window).mean()

        atr = AverageTrueRange(
            df["High"],
            df["Low"],
            df["Close"],
            window=atr_window
        ).average_true_range()

        df["atr"] = atr

        latest = df.iloc[-1]

        if latest["Close"] > latest["ma"]:
            return "trend"
        else:
            return "range"