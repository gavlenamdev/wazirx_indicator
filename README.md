BlockingIOError: [Errno 11] Resource temporarily unavailable
^CException ignored when trying to write to the signal wakeup fd:



System Dependecies:

sudo apt install libgtk-3-dev libgtk-3-0
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
sudo apt install gir1.2-appindicator3-0.1


sudo apt-get install -y python3-venv python3-wheel python3-dev
sudo apt-get install -y libgirepository1.0-dev build-essential \
  libbz2-dev libreadline-dev libssl-dev zlib1g-dev libsqlite3-dev wget \
  curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libcairo2-dev




Runtime dependencies:

glib
libgirepository (gobject-introspection)
libffi
Python 3
The overrides directory contains various files which includes various Python imports mentioning gtk, gdk etc. They are only used when the corresponding library is present, they are not direct dependencies.

Build dependencies:

The runtime dependencies
cairo (optional)
pycairo (optional)
pkg-config
setuptools (optional)
Test Suite dependencies:

The runtime dependencies
GTK 3 (optional)
pango (optional)
pycairo (optional)
