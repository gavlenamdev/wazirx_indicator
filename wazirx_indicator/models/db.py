import sqlite3

from .coin import Coin


class Database:

    def __init__(self):
        self.connection = sqlite3.connect('example.db')

    def create_connection(self):
        pass

    def get_connection(self):
        if self.connection:
            return self.connection
        return sqlite3.connect('example.db')

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE stocks
                       (name text, display_name text, api_index text,symbol text, currency text, current_price real, 
                       low_price real, high_price real, is_favourite boolean)''')
        self.connection.commit()

    def insert(self, coin: Coin):
        cursor = self.connection.cursor()
        query = '''INSERT INTO stocks VALUES("{coin.name}","{coin.display_name}","{coin.api_index}","{coin.symbol}", 
        "{coin.currency}","{coin.current_price}","{coin.low_price}","{coin.high_price}", 
        "{coin.is_favourite}")'''.format(coin=coin)
        cursor.execute(query)
        self.connection.commit()

    def toggle_favourite(self):
        pass