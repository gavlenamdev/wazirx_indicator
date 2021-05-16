import json
import os

import requests

base_url = "https://api.wazirx.com"
api_version = "v2"
base_path = os.path.join(base_url, "api", api_version)
tickers_path = "tickers"


def fetch_current_market():
    try:
        res = requests.get(os.path.join(base_path, tickers_path))
        if res.ok:
            return res.json()
        return {"error": res.reason}
    except requests.exceptions.ConnectionError as e:
        # offline
        print(e)
        return {"error": "ConnectionError"}
    except json.decoder.JSONDecodeError as e:
        # parsing error
        print(e)
        return {"error", "JSONDecodeError"}
    except Exception as e:
        print(e)
        return {"error", "Exception"}


def get_stock_value(data, coin="doge", currency="inr", include_high_low=True):
    if "error" not in data:
        ticker = data[str(coin.lower()) + str(currency.lower())]
        if include_high_low:
            return coin.upper() + ":\t" + ticker["last"] + "  L" + ticker["low"] + "  H" + ticker["high"]
        return coin.upper() + ":  " + ticker["last"]
    return coin.upper()
