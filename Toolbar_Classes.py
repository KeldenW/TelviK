from Widget_Classes import Toolbar_Widget
from Root_Class import Root
import curses


class Toolbar(Root):
    """Class which provides a structure for widgets within a bar"""
    def __init__(self, stdscr, location="top", horizontal_char="=", spacing_char=" "):
        self.stdscr = stdscr
        self.location = location
        self.horizontal_char = horizontal_char
        self.widgets = []
        self.total_space = curses.COLS
        self.current_length = 0
        self.spacing_char = spacing_char
        
        Root.__init__(self)

    def update(self):
        for widget in self.widgets:
            widget.update()

        if self.location == "top":
            self.stdscr.addstr(0, (curses.COLS-self.current_length)//2,
                               f"{self.spacing_char}".join([widget.string for widget in self.widgets]))
            self.stdscr.addstr(1, 0, self.horizontal_char * curses.COLS)
        elif self.location == "bot":
            self.stdscr.addstr(curses.LINES-1, (curses.COLS - self.current_length) // 2,
                               f"{self.spacing_char}".join([widget.string for widget in self.widgets]))
            self.stdscr.addstr(curses.LINES-2, 0, self.horizontal_char * curses.COLS)

    def add_toolbar_widget(self, widget: Toolbar_Widget, index=-1):
        if widget.length + self.current_length > self.total_space:
            return
        self.widgets.insert(index, widget)
        self.current_length += widget.length
