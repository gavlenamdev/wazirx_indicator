import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3 as appindicator

from config import APPLICATION_IDENTIFIER, ICON_PATH, REFRESH_TIME, STOCKS, PRIMARY_STOCK
from wazirx_indicator.helpers import get_stock_value, fetch_current_market


def change_label(indicator, stocks, widgets, primary):
    data = fetch_current_market()
    # print(data)
    indicator.set_label(str(get_stock_value(data, coin=primary, include_high_low=False)), '')
    for widget in widgets:
        stock_name = widget.get_label().lower().split(":")[0]
        stock_data = get_stock_value(data, coin=stock_name)
        widget.set_label(stock_data)
    return True


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        indicator = appindicator.Indicator.new(APPLICATION_IDENTIFIER, ICON_PATH,
                                               appindicator.IndicatorCategory.SYSTEM_SERVICES)
        indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

        # create a menu
        menu = Gtk.Menu()

        menu_item_list = []
        for stock in STOCKS.keys():
            menu_item = Gtk.MenuItem().new_with_label(label=stock.upper())
            menu.append(menu_item)
            menu_item.show_all()
            menu_item_list.append(menu_item)

        separator = Gtk.SeparatorMenuItem()
        menu.append(separator)

        menu_item = Gtk.MenuItem().new_with_label(label="Exit")
        menu.append(menu_item)
        menu_item.connect("activate", self.quit)
        menu_item.show_all()

        # add to indicator
        indicator.set_menu(menu)
        GLib.timeout_add(REFRESH_TIME, change_label, indicator, STOCKS, menu_item_list, PRIMARY_STOCK)
        Gtk.main()

    def quit(self, source):
        Gtk.main_quit()

    def do_startup(self):
        Gtk.Application.do_startup(self)
