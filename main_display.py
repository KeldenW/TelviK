import curses

import Sidebar_Classes
from Toolbar_Classes import *
from Widget_Classes import *
from errors import * 
import logging
from pynput.mouse import Listener
import threading
from logging import info
from time import sleep

logging.basicConfig(filename=r"/home/tankblaster/PycharmProjects/TelviK/logs.log", level=logging.INFO)
root = Root()


def curses_main(stdscr: curses.window):
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
    tool.add_widget(Label("Hello World!"), 1)

    # Main event loop
    while True:
        # get keyboard input, returns -1 if none available
        tool.update()
        Sidebar_Classes.add_todo_list(stdscr, ["Make Breakfast", "Write code", "English!"])
        # return cursor to start position
        stdscr.move(0, 0)
        stdscr.refresh()


def main():
    def on_scroll(x, y, dx, dy):


    with Listener(on_scroll=on_scroll) as listener:
        listener.join()
        listener.start()


    curses.wrapper(curses_main)




if __name__ == "__main__":
    main()
