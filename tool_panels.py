from datetime import datetime
from errors import *
import curses

TOP_PAD = 2
RIGHT_PAD = 20


def add_time_date(stdscr: curses.window):
    today = datetime.now().strftime("%B %d, %Y -- %H:%M:%S")

    for i in range(curses.COLS):
        stdscr.addch(TOP_PAD-1, i, "=".encode("utf-8"))

    stdscr.addstr(TOP_PAD//2-1, (curses.COLS-len(today))//2, today)


def add_todo_list(stdscr: curses.window, things_to_do=[]):
    # TODO Add auto scrolling to todo tasks horizontally and scrolling vertically

    # This is here until the above is implemented
    if len(things_to_do) > curses.LINES-TOP_PAD:
        raise TodoTooLongError(len(things_to_do), curses.LINES-TOP_PAD)

    for y in range(curses.LINES-TOP_PAD):
        stdscr.addch(y+TOP_PAD, curses.COLS-RIGHT_PAD, "|".encode("utf-8"))

    stdscr.addstr(TOP_PAD, curses.COLS-RIGHT_PAD//2-2, "TODO")
    stdscr.addstr(TOP_PAD+1, curses.COLS - RIGHT_PAD+1, "-"*(RIGHT_PAD-1))

    for idx, item in enumerate(things_to_do):
        if len(item) > RIGHT_PAD-1:
            raise ItemTooLongError(len(item), RIGHT_PAD-1)
        stdscr.addstr(TOP_PAD+idx+2, curses.COLS-RIGHT_PAD//2-len(item)//2, item)
