import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3 as appindicator

from config import APPLICATION_IDENTIFIER, ICON_PATH, REFRESH_TIME, STOCKS, PRIMARY_STOCK
from wazirx_indicator.helpers import get_stock_value, fetch_current_market


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)
        self.menu_item_list = []
        self.indicator = appindicator.Indicator.new(APPLICATION_IDENTIFIER, ICON_PATH,
                                                    appindicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

    def do_activate(self):

        # create a menu
        menu = Gtk.Menu()

        for stock in STOCKS.keys():
            menu_item = Gtk.MenuItem().new_with_label(label=stock.upper())
            menu.append(menu_item)
            menu_item.show_all()
            self.menu_item_list.append(menu_item)

        separator = Gtk.SeparatorMenuItem()
        menu.append(separator)

        menu_item = Gtk.MenuItem().new_with_label(label="Exit")
        menu.append(menu_item)
        menu_item.connect("activate", self.quit)
        menu_item.show_all()

        # add to indicator
        self.indicator.set_menu(menu)
        GLib.timeout_add(REFRESH_TIME, self.change_label)
        Gtk.main()

    def quit(self, source):
        Gtk.main_quit()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def change_label(self):
        data = fetch_current_market()
        # print(data)
        self.indicator.set_label(str(get_stock_value(data, coin=PRIMARY_STOCK, include_high_low=False)), '')
        has_error = False
        for menu_item in self.menu_item_list:
            stock_name = menu_item.get_label().lower().split(":")[0]
            print(stock_name)
            print(stock_name == "")
            if stock_name != "":
                stock_label = get_stock_value(data, coin=stock_name)
                menu_item.set_label(stock_label)
            else:
                # stock name is empty means, may be some network error. So break
                has_error = True
                break
        if not has_error:
            return True

        for stock, menu_item in zip(STOCKS.keys(), self.menu_item_list):
            menu_item.set_label(stock.upper())
            menu_item.show_all()
        return True
