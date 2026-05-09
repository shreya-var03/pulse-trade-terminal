import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("PulseTrade")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler = logging.FileHandler("logs/trading.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)