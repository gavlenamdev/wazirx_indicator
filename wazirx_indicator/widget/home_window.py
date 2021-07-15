import json

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk

from .coin_button import CoinButton
from config import COINS_INDEX_FILE_PATH
from ..helpers.wazirx_helper import write_search_keys


@Gtk.Template(filename="wazirx_indicator/ui/home_window.glade")
class HomeWindow(Gtk.Window):
    __gtype_name__ = "homeWindow"

    searchResultView: Gtk.ListBox = Gtk.Template.Child()
    searchBar: Gtk.SearchBar = Gtk.Template.Child()

    def __init__(self, updateMenuItemsList=None, **kwargs):
        super().__init__(**kwargs)
        self.updateMenuItemsList = updateMenuItemsList

        # load index data
        self.index_data = {}
        with open(COINS_INDEX_FILE_PATH) as fd:
            data = fd.read()
            self.index_data = json.loads(data)

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
        # TODO: change image
        write_search_keys()
        # TODO: back to same image

    def onCtrlF(self, widget, event):
        shortcut = Gtk.accelerator_get_label(event.keyval, event.state)

        if shortcut in ("Ctrl+F"):
            if self.searchBar.get_search_mode():
                self.searchBar.set_search_mode(False)
            else:
                self.searchBar.set_search_mode(True)
