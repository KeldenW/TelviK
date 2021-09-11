from datetime import datetime
import curses


def add_time_date(stdscr: curses.window, ):
    today = datetime.now().strftime("%B %d, %Y -- %H:%M:%S")
    print(today)

    for i in range(curses.COLS):
        stdscr.addch(2, i, "#".encode("utf-8"))

    stdscr.addstr(1, (curses.COLS-len(today))//2, today)

