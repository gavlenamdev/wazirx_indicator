import json
import time, threading

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GdkPixbuf

from .widget.coin_button import CoinButton
from .config import COINS_INDEX_FILE_PATH
from .helpers.wazirx_helper import write_search_keys


@Gtk.Template(resource_path='/com/github/gavlenamdev/wazirx_indicator/home_window.ui')
class HomeWindow(Gtk.Window):
    __gtype_name__ = "homeWindow"

    searchResultView: Gtk.ListBox = Gtk.Template.Child()
    searchBar: Gtk.SearchBar = Gtk.Template.Child()
    spinner: Gtk.Spinner = Gtk.Template.Child()

    def __init__(self, updateMenuItemsList=None, **kwargs):
        super().__init__(**kwargs)
        self.updateMenuItemsList = updateMenuItemsList

        # load index data
        self.index_data = {}
        # with open(COINS_INDEX_FILE_PATH) as fd:
        #     data = fd.read()
        #     self.index_data = json.loads(data)

        self.connect("key-press-event", self.onCtrlF)

    def clearSearchResultView(self):
        children = self.searchResultView.get_children()
        for element in children:
            self.searchResultView.remove(element)

    @Gtk.Template.Callback()
    def onSearchEntryChanged(self, widget, **_kwargs):
        self.clearSearchResultView()

        search_text = widget.get_text()
        print(search_text)
        if len(search_text) == 0:
            self.clearSearchResultView()
            return
        results = list(filter(lambda s: search_text.lower() in s.lower(), self.index_data.keys()))
        print(results)

        for result in results[:10]:
            button = CoinButton(result, updateMenuItemsList=self.updateMenuItemsList)
            row = Gtk.ListBoxRow()
            row.add(button)
            self.searchResultView.prepend(row)
            self.searchResultView.show_all()

    @Gtk.Template.Callback()
    def onRefreshButtonClicked(self, widget, **_kwargs):
        print("refresh")
        print(widget)
        t = threading.Thread(target=self.sleep_and_stop, args=())
        self.spinner.start()
        t.start()
        # self.spinner.props.active = True
        # self.spinner.show()
        # print(self.spinner)
        #  time.sleep(1000)
        write_search_keys()
        # self.spinner.stop()

    def sleep_and_stop(self, data = None):

        time.sleep(1);
        print("I'm done");
        self.spinner.stop();

    def onCtrlF(self, widget, event):
        shortcut = Gtk.accelerator_get_label(event.keyval, event.state)

        if shortcut in ("Ctrl+F"):
            if self.searchBar.get_search_mode():
                self.searchBar.set_search_mode(False)
            else:
                self.searchBar.set_search_mode(True)
