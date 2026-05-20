# First Start the  

# Binance Futures Testnet Trading Bot

This is a simple Python trading bot for Binance Futures Testnet.

# Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- CLI input
- Validation
- Error handling
- Logging

## Setup

Install packages:

pip install -r requirements.txt

## Run

Market Order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000

## Assumptions

Using Binance Futures Demo API.

