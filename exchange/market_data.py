from exchange.binance_client import client

def get_order_book(symbol):

    depth = client.futures_order_book(symbol=symbol, limit=5)

    bids = depth["bids"]
    asks = depth["asks"]

    return bids, asks

def get_mark_price(symbol):

    data = client.futures_mark_price(symbol=symbol)
    return float(data["markPrice"])