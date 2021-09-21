import curses

import Sidebar_Class
from Toolbar_Class import *
from Widget_Classes import *
from errors import * 
import logging
from pynput.mouse import Listener
import threading
from logging import info
from time import sleep

logging.basicConfig(filename=r"logs.log", level=logging.INFO)


def curses_main(stdscr: curses.window):

    root = Root()

    stdscr.nodelay(True)
    curses.curs_set(0)
    curses.mousemask(1)
    if curses.COLS < root.min_length:
        raise TerminalTooThinError(curses.COLS, root.min_length)
    elif curses.LINES < root.min_height:
        raise TerminalTooShortError(curses.LINES, root.min_height)

    # Adding things to the screen
    tool = Toolbar(stdscr, "top")
    tool.add_widget(Date_Time(), -1)
    tool.add_widget(Label("Hello!"), 1)

    # Main event loop
    while True:
        tool.update()
        # return cursor to start position
        stdscr.move(0, 0)
        stdscr.refresh()


def main():
    curses.wrapper(curses_main)


if __name__ == "__main__":
    main()
