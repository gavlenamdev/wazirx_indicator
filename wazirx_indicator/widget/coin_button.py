import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from ..models.files import append_to_favourites


class CoinButton(Gtk.Button):

    def __init__(self, label: str, checked=False, updateMenuItemsList=None):
        super(CoinButton, self).__init__('')
        self.updateMenuItemsList = updateMenuItemsList

        image = Gtk.Image()
        image.set_property("visible", True)
        image.set_property("can_focus", True)
        image.set_property("stock", 'gtk-add')

        self.image_checked = Gtk.Image()
        self.image_checked.set_property("visible", True)
        self.image_checked.set_property("can_focus", True)
        self.image_checked.set_property("stock", 'gtk-apply')

        self.set_property("label", label)
        self.set_property("visible", True)
        self.set_property("can_focus", True)
        self.set_property("receives_default", True)
        self.set_property("always_show_image", True)
        if checked:
            self.set_property("image", self.image_checked)
        else:
            self.set_property("image", image)

        self.connect("clicked", self.onCoinButtonClicked)

    def onCoinButtonClicked(self, widget, **_kwargs):
        index = widget.get_label()
        append_to_favourites(index)
        self.set_property("image", self.image_checked)
        # TODO: event to update stocks value in indicator
        # self.emit("update_favourites")
        self.updateMenuItemsList(index)
