import threading
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk

from ..models.files import write_to_primary, reformat_favourites, read_primary, read_favourites
from wazirx_indicator import get_stock_value, fetch_current_market
from config import STOCKS, PRIMARY_STOCK


class IndicatorMenu(Gtk.Menu):

    def __init__(self, parent=None):
        super(IndicatorMenu, self).__init__()
        self.parent = parent
        self.menu_item_list = []
        reformat_favourites()
        self.stocks = read_favourites() or STOCKS
        self.primary_stock = read_primary() or PRIMARY_STOCK

        for stock in self.stocks:
            menu_item = Gtk.MenuItem().new_with_label(label=stock.upper())
            menu_item.connect("activate", self.set_as_primary)
            self.append(menu_item)
            menu_item.show_all()
            self.menu_item_list.append(menu_item)
        # separator
        separator = Gtk.SeparatorMenuItem()
        self.append(separator)
        # app menus
        # open app
        menu_item = Gtk.MenuItem().new_with_label(label="Open")
        self.append(menu_item)
        menu_item.connect("activate", self.parent.open)
        menu_item.show_all()
        # exit menu
        menu_item = Gtk.MenuItem().new_with_label(label="Exit")
        self.append(menu_item)
        menu_item.connect("activate", self.parent.quit)
        menu_item.show_all()

    def updateFavourites(self):
        self.stocks = read_favourites()

    def updateMenuItemsList(self, stock):
        print("updateMenuItemsList")
        menu_item = Gtk.MenuItem().new_with_label(label=stock.upper())
        menu_item.connect("activate", self.set_as_primary)
        self.append(menu_item)
        menu_item.show_all()
        self.menu_item_list.append(menu_item)

    def change_label(self):
        data = fetch_current_market()
        prime_stock_price = get_stock_value(data, self.primary_stock, include_high_low=False)
        self.parent.indicator.set_label(prime_stock_price, '')
        has_error = False
        for menu_item in self.menu_item_list:
            stock_name = menu_item.get_label().lower().split(":")[0]
            # print(stock_name)
            # print(stock_name == "")
            if stock_name != "":
                stock_label = get_stock_value(data, stock_name)
                menu_item.set_label(stock_label)

            else:
                # stock name is empty means, may be some network error. So break
                has_error = True
                break
        if not has_error:
            return True

        temp_menu_item_list = []
        for stock, menu_item in zip(self.stocks, self.menu_item_list):
            menu_item.set_label(stock.upper())
            # menu_item.connect("activate", self.set_as_primary)
            menu_item.show_all()
            temp_menu_item_list.append(menu_item)
        self.menu_item_list = temp_menu_item_list
        return True

    def change_label_async(self):
        thread = threading.Thread(target=self.change_label, daemon=True)
        thread.start()

    def set_as_primary(self, menu_item):
        stock_name = menu_item.get_label().lower().split(":")[0]
        print(stock_name)
        self.primary_stock = stock_name
        write_to_primary(stock_name)
