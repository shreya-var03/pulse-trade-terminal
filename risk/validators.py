from core.exceptions import ValidationError

VALID_SIDES = ["BUY", "SELL"]
VALID_TYPES = ["MARKET", "LIMIT"]

def validate_order(symbol, side, order_type, quantity, price=None):

    if side not in VALID_SIDES:
        raise ValidationError("Invalid side")

    if order_type not in VALID_TYPES:
        raise ValidationError("Invalid order type")

    if quantity <= 0:
        raise ValidationError("Quantity must be positive")

    if order_type == "LIMIT" and not price:
        raise ValidationError("LIMIT orders require price")

    if not symbol.endswith("USDT"):
        raise ValidationError("Only USDT pairs supported")