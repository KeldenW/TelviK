from errors import *
from Widget_Classes import *
from Root_Class import Root
import curses


class Sidebar(Root):
    def __init__(self, stdscr: curses.window, location="right", widgets=None):
        if widgets is None:
            self.widgets = []
        self.stdscr = stdscr
        self.location = location
        Root.__init__(self)

    def update(self):
        for widget in self.widgets:
            widget.update()

    def add_side_widget(self, widget: Side_Widget, index=-1):
        self.widgets.insert(index, widget)
