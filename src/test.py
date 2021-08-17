import os
import sys
import signal
import gettext

VERSION = '@VERSION@'
pkgdatadir = '@pkgdatadir@'
localedir = '@localedir@'

sys.path.insert(1, pkgdatadir)
sys.path.insert(1, "/home/plugxr/Projects/wazirx_indicator/env/lib/python3.8/site-packages")
signal.signal(signal.SIGINT, signal.SIG_DFL)
gettext.install('wazirx_indicator', localedir)

if __name__ == '__main__':
    import gi

    from gi.repository import Gio
    resource = Gio.Resource.load(os.path.join(pkgdatadir, 'wazirx_indicator.gresource'))
    resource._register()

    from wazirx_indicator import main
    sys.exit(main.main(VERSION))