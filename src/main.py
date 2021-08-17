
import sys
import logging
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib, Gio, GObject
# from gi.repository import AppIndicator3 as appindicator


from .config import APPLICATION_IDENTIFIER, ICON_PATH, REFRESH_TIME, PRIMARY_STOCK
from .helpers import get_stock_value, fetch_current_market
from .home_window import HomeWindow
from .widget.indicator_menu import IndicatorMenu
from .models.files import reformat_favourites, read_favourites, read_primary

import site;
import sysconfig;


try:
    try:
        gi.require_version("AyatanaAppIndicator3", "0.1")
        from gi.repository import AyatanaAppIndicator3 as appindicator  # pylint: disable=E0611

        _indicator_backend = "AyatanaAppIndicator3"  # Just a dummy value we use for logging
    except (ValueError, ImportError) as e:
        print(e)
        gi.require_version("AppIndicator3", "0.1")
        from gi.repository import AppIndicator3 as appindicator # pylint: disable=E0611

        _indicator_backend = "AppIndicator3"
    use_appindicator = True
except (ValueError, ImportError) as e:
    print(e)
    print("app indicator does not support")
    print(site.getsitepackages())
    print(sysconfig.get_paths()["purelib"])
    # /usr/lib/python3.9/site-packages
    _indicator_backend = "fallback tray"
    use_appindicator = False

logger = logging.getLogger(__name__)

#if appindicator is None:
#    logger.warning("AppIndicator3 is not installed. The App indicator will not be shown.")

class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.github.gavlenamdev.wazirx_indicator',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.status_icon = None
        self.indicator = None

        if use_appindicator:

            self.indicator = appindicator.Indicator.new(APPLICATION_IDENTIFIER, ICON_PATH,
                                                    appindicator.IndicatorCategory.SYSTEM_SERVICES)
            self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        else:
            print("no support for app indicator")
            self.status_icon = Gtk.StatusIcon.new_from_file("/home/plugxr/Projects/wazirx_indicator/data/icons/hicolor/scalable/apps/com.github.gavlenamdev.wazirx_indicator.svg")
            self.status_icon.set_visible(True)
            # self.status_icon.connect("activate", left_click_event)
            # self.status_icon.connect("popup-menu", right_click_event)
            # self.status_icon.connect("scroll-event", on_indicator_scroll_status_icon)

        #except (ImportError, ValueError):
            #self.appindicator_support = False
            #self.indicator = Gtk.StatusIcon()
            #self.indicator.set_from_stock(Gtk.STOCK_HOME)
            # self.ind.set_from_file(icon)




    def do_activate(self):
        # win = self.props.active_window
        # if not win:
        #     win = WazirxIndicatorWindow(application=self)
        # win.present()
        # menu
        menu = IndicatorMenu(parent=self)

        if use_appindicator:
            self.indicator.set_menu(menu)
        else:
            # self.status_icon.position_menu(menu, 0, 0, self.indicator)
            menu.popup(None, None, Gtk.StatusIcon.position_menu, self.status_icon, 0, Gtk.get_current_event_time())

        # home window
        self.window = HomeWindow(application=self, updateMenuItemsList=[])
        self.window.show_all()

        GLib.timeout_add(REFRESH_TIME, self.sample_function)
        Gtk.main()

    def sample_function(self):
        pass

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


def main(version):
    app = Application()
    return app.run(sys.argv)
