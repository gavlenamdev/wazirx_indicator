import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, GLib, Gio, GObject
from gi.repository import AppIndicator3 as appindicator

from config import APPLICATION_IDENTIFIER, ICON_PATH, REFRESH_TIME, PRIMARY_STOCK
from wazirx_indicator.helpers import get_stock_value, fetch_current_market
from .widget.home_window import HomeWindow
from .widget.indicator_menu import IndicatorMenu
from .models.files import reformat_favourites, read_favourites, read_primary


class MyApplication(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="com.gavlenamdev.wazirx_notifier",
                         flags=Gio.ApplicationFlags.FLAGS_NONE, **kwargs)
        self.window = None
        self.menu_item_list = []
        self.indicator = appindicator.Indicator.new(APPLICATION_IDENTIFIER, ICON_PATH,
                                                    appindicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

    def do_activate(self):
        # menu
        menu = IndicatorMenu(parent=self)
        self.indicator.set_menu(menu)
        # home window
        self.window = HomeWindow(application=self, updateMenuItemsList=menu.updateMenuItemsList)
        self.window.show_all()

        GLib.timeout_add(REFRESH_TIME, menu.change_label)
        Gtk.main()

    def quit(self, *args, **kwargs):
        Gtk.main_quit(*args, **kwargs)
        # Gtk.Application.

    def open(self, *args, **kwargs):
        self.window = HomeWindow(application=self)
        self.window.show_all()

    def onDestroy(self, *args):
        # quit the application on closing of main application window
        Gtk.main_quit()

    def do_startup(self):
        Gtk.Application.do_startup(self)
