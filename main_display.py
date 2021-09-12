import logging
from Sidebar_Classes import *
from Toolbar_Classes import *
from Widget_Classes import *
from errors import *

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
    side = Sidebar(stdscr, "right")

    tool.add_toolbar_widget(Tool_Date_Time(), -1)
    tool.add_toolbar_widget(Tool_Label("Hello World!"), 1)
    
    side.add_side_widget(Side_Todo_List(stdscr, ["Lorem", "ipsum", "dolor", "sit amet"]))

    # Main event loop
    while True:
        # get keyboard input, returns -1 if none available
        tool.update()
        side.update()
        # return cursor to start position
        stdscr.move(0, 0)
        root.character_response(stdscr)
        stdscr.refresh()


def main():
    curses.wrapper(curses_main)


if __name__ == "__main__":
    main()
