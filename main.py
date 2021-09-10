import curses
from time import sleep


def main(stdscr):
    print(curses.COLS, curses.LINES)


if __name__ == "__main__":
    curses.wrapper(main)
