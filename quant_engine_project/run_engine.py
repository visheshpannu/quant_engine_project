import json
import pandas as pd
from engine.core.engine import BacktestEngine

def main():

    with open("configs/engine.json") as f:
        config = json.load(f)

    df = pd.read_csv(config["data_file"], index_col=0, parse_dates=True)

    engine = BacktestEngine(config)
    trades = engine.run(df)

    pd.DataFrame(trades, columns=["pnl"]).to_excel("outputs/orders.xlsx", index=False)

    print("Backtest completed!")

if __name__ == "__main__":
    main()