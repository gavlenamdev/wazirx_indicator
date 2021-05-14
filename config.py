import os

APPLICATION_IDENTIFIER = 'wazirx_indicator'
PROJECT_DIR = os.path.dirname(__file__)
ICON_PATH = os.path.join(PROJECT_DIR, "assets", "img", "wazirx_icon.png")
REFRESH_TIME = 4000

STOCKS = {
    "doge": {"currency": "INR", "current_price": "..."},
    "wrx": {"currency": "INR", "current_price": "..."},
    "shib": {"currency": "INR", "current_price": "..."},
    "trx": {"currency": "INR", "current_price": "..."},
    "zrx": {"currency": "INR", "current_price": "..."},
    "vet": {"currency": "INR", "current_price": "..."},
    "hbar": {"currency": "INR", "current_price": "..."},
    "matic": {"currency": "INR", "current_price": "..."},
    "ada": {"currency": "INR", "current_price": "..."},
    "ftm": {"currency": "INR", "current_price": "..."},
    "eth": {"currency": "INR", "current_price": "..."},
    "sc": {"currency": "INR", "current_price": "..."}
}

PRIMARY_STOCK = "doge"
