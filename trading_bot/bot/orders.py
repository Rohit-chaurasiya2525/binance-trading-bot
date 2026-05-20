import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        if order_type.upper() == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logging.info(f"Request: {params}")

        response = client.futures_create_order(**params)

        logging.info(f"Response: {response}")

        return response

    except Exception as e:
        logging.error(str(e))
        raise