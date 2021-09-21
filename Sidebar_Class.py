from errors import *
from Widget_Classes import *
from Root_Class import Root
import curses
from logging import info


class Sidebar(Root):
    def __init__(self, stdscr: curses.window, location="right", widgets=None, vertical_char="|"):
        info("Initalizing Sidebar")
        if widgets is None:
            self.widgets = []
        self.vertical_char = vertical_char
        self.stdscr = stdscr
        self.location = location

    def update(self):
        for widget in self.widgets:
            widget.update()

        if self.location == "right":
            for y in range(curses.LINES-self.top_pad):
                self.stdscr.addch(y+self.top_pad, curses.COLS-self.right_pad, self.vertical_char)
        elif self.location == "left":
            for y in range(curses.LINES-self.top_pad):
                self.stdscr.addch(y+self.top_pad, self.right_pad, self.vertical_char)

    def add_side_widget(self, widget, index=-1):
        self.widgets.insert(index, widget)