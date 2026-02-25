import pandas as pd
from ..regimes.regime_classifier import RegimeClassifier
from ..factory.strategy_factory import StrategyFactory

class BacktestEngine:

    def __init__(self, config):
        self.config = config

    def run(self, df):

        regime_detector = RegimeClassifier(
            self.config["regime_classifier"]
        )

        regime = regime_detector.detect(df)

        strat_key = "trend_following"

        strat_config = self.config["strategies"][strat_key]

        strategy = StrategyFactory.load_strategy(
            strat_config["logic_id"],
            strat_config["params"]
        )

        df = strategy.generate_signals(df)

        trades = []
        position = None

        for i in range(1, len(df)):

            signal = df["signal"].iloc[i]

            if signal == 1 and position is None:
                entry_price = df["Open"].iloc[i]
                position = entry_price

            elif signal == -1 and position is not None:
                exit_price = df["Open"].iloc[i]
                pnl = exit_price - position
                trades.append(pnl)
                position = None

        return trades