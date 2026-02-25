# quant_engine_project
A configurable quantitative trading backtesting engine built in Python. Supports strategy execution, trade generation, and performance export using clean modular architecture.
📊 Quantitative Trading Backtesting Engine

A modular and configurable quantitative trading backtesting engine built using Python.
This project allows users to test trading strategies on historical market data and export performance results.

🚀 Features

📈 Historical data loading (CSV-based)

⚙️ JSON-based configuration system

🧠 Strategy execution via Backtest Engine

📊 Trade PnL calculation

📁 Excel export of backtest results

🧩 Clean and modular architecture

🏗 Project Structure
quant_engine_project/
│
├── configs/
│   └── engine.json
│
├── data/
│   └── ohlc_clean.csv
│
├── engine/
│   ├── core/
│   └── utils/
│
├── outputs/
│   └── orders.xlsx
│
├── fetch_data.py
├── run_engine.py
└── README.md
⚡ How It Works
1️⃣ Fetch Market Data

The file fetch_data.py downloads and cleans historical OHLC data.

📄 File: 

fetch_data

Run:

python fetch_data.py

This saves cleaned data into:

data/ohlc_clean.csv
2️⃣ Run Backtest Engine

The main execution script is:

📄 File: 

run_engine

Run:

python run_engine.py
What Happens Internally?

Loads configuration from configs/engine.json

Reads historical data

Initializes BacktestEngine

Executes strategy logic

Generates trade results

Exports PnL to:

outputs/orders.xlsx
🛠 Technologies Used

Python 3.x

Pandas

JSON configuration

Excel export (openpyxl/xlsxwriter)

🧠 Architecture Overview
Market Data → Data Loader → Backtest Engine → Strategy Logic → Trade Output → Excel Report

The system is designed to be:

Extensible (add new strategies easily)

Config-driven

Clean separation of concerns

📌 Example Workflow

Configure strategy parameters in engine.json

Fetch market data

Run backtest

Analyze exported trade PnL in Excel

🔮 Future Improvements

Performance metrics (Sharpe ratio, drawdown)

Multi-strategy support

Portfolio-level backtesting

Visualization dashboard

Risk management module

🎯 Use Cases

Learning quantitative trading

Strategy prototyping

Backtesting academic trading models

Portfolio research projects

📬 Author

Vishesh Singh
Computer Science Student | Quant & Backend Developer
Focused on systematic trading systems and financial engineering.
