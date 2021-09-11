import curses
from errors import *
import tool_panels
from time import sleep

# Global Constants
MIN_COLS = 25
MIN_LINES = 5


def curses_main(stdscr: curses.window):
    stdscr.nodelay(True)
    curses.curs_set(0)
    if curses.COLS < MIN_COLS:
        raise TerminalTooThinError(curses.COLS, MIN_COLS)
    elif curses.LINES < MIN_LINES:
        raise TerminalTooShortError(curses.LINES, MIN_LINES)

    # Main event loop
    while True:
        # get keyboard input, returns -1 if none available
        tool_panels.add_time_date(stdscr)
        tool_panels.add_todo_list(stdscr, ["Make Breakfast", "Write code", "English!"])
        key = stdscr.getch()
        if key != -1:
            if chr(key) == "q":
                break
            # return cursor to start position
            stdscr.move(0, 0)

        stdscr.refresh()


def main():
    curses.wrapper(curses_main)


if __name__ == "__main__":
    main()
