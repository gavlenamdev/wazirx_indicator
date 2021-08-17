from ..config import FAVOURITE_COINS_FILE_PATH, PRIMARY_COIN_FILE_PATH


def write_to_favourites(stock):
    with open(FAVOURITE_COINS_FILE_PATH, "w") as fd:
        fd.write(stock)


def read_favourites():
    try:
        with open(FAVOURITE_COINS_FILE_PATH, "r") as fd:
            data = fd.readlines()
            final_list = []
            for d in data:
                if len(d.strip()) > 0:
                    final_list.append(d.strip())
            return final_list
    except:
        return []


def append_to_favourites(stock):
    with open(FAVOURITE_COINS_FILE_PATH, "a") as fd:
        fd.write(stock + "\n")


def reformat_favourites():
    data = read_favourites()
    data = set(data)
    data = '\n'.join(data) + "\n"
    write_to_favourites(data)


def write_to_primary(stock):
    with open(PRIMARY_COIN_FILE_PATH, "w") as fd:
        fd.write(stock + "\n")


def read_primary():
    try:
        with open(PRIMARY_COIN_FILE_PATH, "r") as fd:
            data = fd.readlines()
            return data[0].strip()
    except:
        return
