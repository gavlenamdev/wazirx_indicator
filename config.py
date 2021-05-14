import os

APPLICATION_IDENTIFIER = 'wazirx_indicator'
PROJECT_DIR = os.path.dirname(__file__)
ICON_PATH = os.path.join(PROJECT_DIR, "assets", "img", "wazirx_icon.png")
REFRESH_TIME = 4000

STOCKS = {
    "doge": {"currency": "INR", "current_price": "..."},
    "wrx": {"currency": "INR", "current_price": "..."}
}

PRIMARY_STOCK = "doge"
