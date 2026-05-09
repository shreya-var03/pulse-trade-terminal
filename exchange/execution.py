import time

from exchange.binance_client import client
from core.logger import logger

def place_order(symbol, side, order_type, quantity, price=None):

    start = time.time()

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    try:

        logger.info(f"ORDER REQUEST: {params}")

        response = client.futures_create_order(**params)

        latency = round((time.time() - start) * 1000, 2)

        logger.info(f"ORDER RESPONSE: {response}")
        logger.info(f"LATENCY: {latency} ms")

        return response, latency

    except Exception as e:

        logger.error(f"ERROR: {str(e)}")
        raise