
from gi.repository import Gtk


@Gtk.Template(resource_path='/com/github/gavlenamdev/wazirx_indicator/window.ui')
class WazirxIndicatorWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'WazirxIndicatorWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
