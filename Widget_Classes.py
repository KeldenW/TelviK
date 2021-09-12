import curses
from datetime import datetime
from Root_Class import Root
from errors import *
from pynput.mouse import Listener
import logging
from logging import info
import tkinter as tk
import ctypes


logging.basicConfig(filename=r"logs.log", level=logging.INFO)

# We Start off with Toolbar Widgets


class Toolbar_Widget(Root):
    """Organizational class for widgets"""

    def __init__(self, string: str, length: int):
        self.string = string
        self.length = length
        
        Root.__init__(self)


class Tool_Date_Time(Toolbar_Widget):
    """A widget that returns a string of the current date and time in the specified format"""

    def __init__(self, date_time_format="%B %d, %Y -- %H:%M:%S"):
        self.date_time_format = date_time_format
        self.length = 0
        self.string = ""
        self.update()
        Toolbar_Widget.__init__(self, self.string, len(self.string))

    def update(self):
        self.string = datetime.now().strftime(self.date_time_format)
        self.length = len(self.string)


class Tool_Label(Toolbar_Widget):
    """A Widget which returns a user defined label"""
    def __init__(self, message=""):
        Toolbar_Widget.__init__(self, message, len(message))

    def update(self):
        pass


# Now for the Sidebar Widgets


class Side_Widget(Root):
    def __init__(self, height=0):

        self.height = height


class Side_Todo_List(Side_Widget):
    def __init__(self, stdscr: curses.window, tasks=None):
        self.tasks = [] if tasks is None else None
        self.stdscr = stdscr

        # Get the screen resolution so we can detect where someone is scrolling
        t_root = tk.Tk()

        screen_width = t_root.winfo_screenwidth()
        screen_height = t_root.winfo_screenheight()

        # Make sure we are maximized
        user32 = ctypes.WinDLL('user32')

        SW_MAXIMISE = 3

        hWnd = user32.GetForegroundWindow()

        user32.ShowWindow(hWnd, SW_MAXIMISE)

        with Listener(on_scroll=self.on_scroll) as listener:
            listener.join()
            listener.start()

    def on_scroll(self, x, y, dx, dy):
        info(self.stdscr.getparyx())


def add_todo_list(stdscr: curses.window, things_to_do=None):
    # TODO Add auto scrolling to todo tasks horizontally and scrolling vertically

    if things_to_do is None:
        things_to_do = []

    # This is here until the above comment is implemented
    if len(things_to_do) > curses.LINES-Root().top_pad:
        raise TodoTooLongError(len(things_to_do), curses.LINES - Root().top_pad)

    for y in range(curses.LINES - Root().top_pad):
        stdscr.addch(y + Root().top_pad, curses.COLS - Root().right_pad, "|".encode("utf-8"))

    stdscr.addstr(Root().top_pad, curses.COLS - Root().right_pad // 2 - 2, "TODO")
    stdscr.addstr(Root().top_pad + 1, curses.COLS - Root().right_pad + 1, "-" * (Root().right_pad - 1))

    for idx, item in enumerate(things_to_do):
        if len(item) > Root().right_pad-1:
            raise ItemTooLongError(len(item), Root().right_pad - 1)
        stdscr.addstr(Root().top_pad + idx + 2, curses.COLS - Root().right_pad // 2 - len(item) // 2, item)
