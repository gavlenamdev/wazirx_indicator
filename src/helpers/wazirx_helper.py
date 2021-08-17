import json
import os

import requests

from ..config import COINS_INDEX_FILE_PATH

base_url = "https://api.wazirx.com"
api_version = "v2"
base_path = os.path.join(base_url, "api", api_version)
tickers_path = "tickers"


def fetch_current_market():
    try:
        res = requests.get(os.path.join(base_path, tickers_path))
        print(res, res.reason)
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


def get_stock_value(data, name, include_high_low=True):
    coin = name.split("/")[0]
    currency = name.split("/")[1]
    if "error" not in data:
        ticker = data[str(coin.lower()) + str(currency.lower())]
        if include_high_low:
            return name.upper() + ":\t" + ticker["last"] + "  L" + ticker["low"] + "  H" + ticker["high"]
        return name.upper() + ":  " + ticker["last"]
    return name.upper()


def get_stocks_list() -> dict:
    data = fetch_current_market()
    if 'error' not in data:
        print("no errors")
        values = list(map(lambda v: v['name'], data.values()))
        return dict(zip(values, data.keys()))
    return {}


def write_search_keys():
    data = get_stocks_list()
    with open(COINS_INDEX_FILE_PATH, "w+") as fd:
        formatted_data = json.dumps(data, sort_keys=True, indent=2)
        print(formatted_data)
        fd.write(formatted_data)
        print("wrote index")


# print(write_search_keys())
