import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser(description="Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_order(args.type, args.price)

    client = get_client()

    result = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nOrder Request Success")
    print(result)

except Exception as e:
    print("Failed:", e)