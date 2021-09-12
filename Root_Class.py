import curses
import platform
from logging import info


class Root:
    def __init__(self, top_pad=2, right_pad=20, bottom_pad=2, left_pad=20, main_length=25, main_height=5):
        self.top_pad = top_pad
        self.right_pad = right_pad
        self.bottom_pad = bottom_pad
        self.left_pad = left_pad
        self.min_length = left_pad + main_length + right_pad
        self.min_height = top_pad + main_height + bottom_pad
        self.os_name = platform.system()

        info(self.os_name)

    def character_response(self, stdscr: curses.window):
        char = stdscr.getch()
        if char == ord("q"):
            exit()

