import os

APPLICATION_NAME = "wazirx_indicator"
APPLICATION_IDENTIFIER = 'org.gavlenamdev.wazirx_indicator'
PROJECT_DIR = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(PROJECT_DIR, "assets")
os.makedirs(ASSETS_PATH, exist_ok=True)
ICON_PATH = os.path.join(ASSETS_PATH, "img", "wazirx_icon.png")
COINS_FILE_PATH = os.path.join(ASSETS_PATH, "files.txt")
COINS_INDEX_FILE_PATH = os.path.join(ASSETS_PATH, "index.json")
FAVOURITE_COINS_FILE_PATH = os.path.join(ASSETS_PATH, "favourites.txt")
PRIMARY_COIN_FILE_PATH = os.path.join(ASSETS_PATH, "primary.txt")
REFRESH_TIME = 4000

STOCKS = ["doge/inr", "wrx/inr", "shib/inr", "trx/inr", "zrx/inr", "vet/inr", "hbar/inr", "matic/inr", "ada/inr",
          "ftm/inr", "eth/inr", "btc/inr", "sc/inr"]

PRIMARY_STOCK = "doge/inr"
