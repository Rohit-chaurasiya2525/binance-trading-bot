# Binance Futures Testnet Trading Bot

A simple Python trading bot for Binance Futures Testnet.

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- CLI based input
- Input validation
- Logging
- Error handling

## Setup

Install dependencies:

pip install -r requirements.txt

## Run

Market Order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000

## Project Structure

trading_bot/
├── bot/
├── cli.py
├── requirements.txt
├── README.md
└── bot.log
