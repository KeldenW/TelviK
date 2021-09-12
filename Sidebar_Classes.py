from errors import *
from Root_Class import Root
import curses


class Sidebar(Root):
    def __init__(self):

        Root.__init__(self)


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
