from .strategy_base import StrategyBase

class STRAT_1(StrategyBase):

    def generate_signals(self, df):

        fast = self.params["fast_ma"]
        slow = self.params["slow_ma"]

        df["fast"] = df["Close"].rolling(fast).mean()
        df["slow"] = df["Close"].rolling(slow).mean()

        df["signal"] = 0

        df.loc[df["fast"] > df["slow"], "signal"] = 1
        df.loc[df["fast"] < df["slow"], "signal"] = -1

        df["signal"] = df["signal"].shift(1)

        return df