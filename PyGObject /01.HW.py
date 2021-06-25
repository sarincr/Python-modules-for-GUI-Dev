import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
ob1 = Gtk.Window(title="Hello World")
ob1.show()
ob1.connect("destroy", Gtk.main_quit)
Gtk.main()
