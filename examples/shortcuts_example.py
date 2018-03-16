import sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk

SHORTCUTS = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <!-- interface-requires gtk+ 3.19 -->
  <object id="main" class="GtkShortcutsWindow">
    <property name="modal">true</property>
    <child>
      <object class="GtkShortcutsSection">
            <property name="visible">true</property>
            <property name="section-name">other</property>
            <property name="title" translatable="yes" context="shortcut window">Other stuff</property>
            <child>
          <object class="GtkShortcutsGroup">
            <property name="visible">true</property>
            <property name="title" translatable="yes" context="shortcut window">Selections</property>
            <child>
              <object class="GtkShortcutsShortcut">
                <property name="visible">true</property>
                <property name="accelerator">&lt;ctrl&gt;a</property>
                <property name="title" translatable="yes" context="shortcut window">Select all</property>
              </object>
            </child>
            <child>
              <object class="GtkShortcutsShortcut">
                <property name="visible">true</property>
                <property name="accelerator">&lt;ctrl&gt;backslash</property>
                <property name="title" translatable="yes" context="shortcut window">Unselect all</property>
              </object>
            </child>
          </object>
        </child>
      </object>
      <object class="GtkShortcutsSection">
        <property name="visible">true</property>
        <property name="section-name">editor</property>
        <property name="title" translatable="yes" context="shortcut window">Editor Shortcuts</property>
        
         <child>
          <object class="GtkShortcutsGroup">
            <property name="visible">true</property>
            <property name="title" translatable="yes" context="shortcut window">Touchpad gestures</property>
            <child>
              <object class="GtkShortcutsShortcut">
                <property name="visible">true</property>
                <property name="shortcut-type">gesture-two-finger-swipe-right</property>
                <property name="title" translatable="yes" context="shortcut window">Switch to the next document</property>
              </object>
            </child>
            <child>
              <object class="GtkShortcutsShortcut">
                <property name="visible">true</property>
                <property name="shortcut-type">gesture-two-finger-swipe-left</property>
                <property name="title" translatable="yes" context="shortcut window">Switch to the previous document</property>
              </object>
            </child>
          </object>
        </child>
        <child>
            <object class="GtkShortcutsGroup">
              <property name="visible">true</property>
              <property name="title" translatable="yes" context="shortcut window">Build and Run</property>
              <child>
                <object class="GtkShortcutsShortcut">
                  <property name="visible">true</property>
                  <property name="accelerator">&lt;ctrl&gt;F7</property>
                   <property name="title" translatable="yes" context="shortcut window">Build</property>
                </object>
              </child>
              <child>
                <object class="GtkShortcutsShortcut">
                  <property name="visible">true</property>
                  <property name="accelerator">&lt;ctrl&gt;F5</property>
                  <property name="title" translatable="yes" context="shortcut window">Run</property>
                </object>
              </child>
              <child>
                <object class="GtkShortcutsShortcut">
                  <property name="visible">true</property>
                  <property name="accelerator">&lt;ctrl&gt;F8</property>
                  <property name="title" translatable="yes" context="shortcut window">Profile</property>
                </object>
              </child>
            </object>
        </child>
      </object>
    </child>
  </object>
</interface>
 """


class ExampleWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Shortcut Demo")
        self.set_border_width(10)

        button = Gtk.Button.new_with_label("Click Me")
        button.connect("clicked", self.on_click)
        self.add(button)

    def on_click(self, button):
        builder = Gtk.Builder.new_from_string(SHORTCUTS, -1)

        menu = builder.get_object("main")
        menu.present()

win = ExampleWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()