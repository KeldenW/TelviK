class Root:
    def __init__(self, stdscr, top_pad=2, right_pad=20, bottom_pad=2, left_pad=20, main_length=25, main_height=5):
        self.stdscr = stdscr
        self.top_pad = top_pad
        self.right_pad = right_pad
        self.bottom_pad = bottom_pad
        self.left_pad = left_pad
        self.min_length = left_pad + main_length + right_pad
        self.min_height = top_pad + main_height + bottom_pad
        self.os_name = platform.system()

    def character_response(self):
        char = self.stdscr.getch()
        if char == ord("q"):
            exit()

    class Toolbar(Root):
        """Class which provides a structure for widgets within a bar"""

        def __init__(self, location="top", horizontal_char="=", spacing_char=" "):
            info("Initializing toolbar")
            self.location = location
            self.horizontal_char = horizontal_char
            self.widgets = []
            self.total_space = curses.COLS
            self.current_length = 0
            self.spacing_char = spacing_char

        def update(self):
            for widget in self.widgets:
                widget.update()

            if self.location == "top":
                self.stdscr.addstr(0, (curses.COLS - self.current_length) // 2,
                                   f"{self.spacing_char}".join([widget.string for widget in self.widgets]))
                self.stdscr.addstr(1, 0, self.horizontal_char * curses.COLS)
            elif self.location == "bot":
                self.stdscr.addstr(curses.LINES - 1, (curses.COLS - self.current_length) // 2,
                                   f"{self.spacing_char}".join([widget.string for widget in self.widgets]))
                self.stdscr.addstr(curses.LINES - 2, 0, self.horizontal_char * curses.COLS)

        def add_toolbar_widget(self, widget: ToolbarWidget, index=-1):
            if widget.length + self.current_length > self.total_space:
                return
            self.widgets.insert(index, widget)
            self.current_length += widget.length

    class Sidebar(Root):
        def __init__(self, stdscr: curses.window, location="right", widgets=None, vertical_char="|"):
            info("Initializing Sidebar")
            if widgets is None:
                self.widgets = []
            self.vertical_char = vertical_char
            self.stdscr = stdscr
            self.location = location

        def update(self):
            for widget in self.widgets:
                widget.update()

            if self.location == "right":
                for y in range(curses.LINES - self.top_pad):
                    self.stdscr.addch(y + self.top_pad, curses.COLS - self.right_pad, self.vertical_char)
            elif self.location == "left":
                for y in range(curses.LINES - self.top_pad):
                    self.stdscr.addch(y + self.top_pad, self.right_pad, self.vertical_char)

        def add_side_widget(self, widget: SideWidget, index=-1):
            self.widgets.insert(index, widget)

    class ToolbarWidget(Root):
        """Organizational class for widgets"""

        def __init__(self, string: str, length: int):
            info("Initializing ToolbarWidget class")
            self.string = string
            self.length = length

        class ToolDateTime(ToolbarWidget):
            """A widget that returns a string of the current date and time in the specified format"""

            def __init__(self, date_time_format="%B %d, %Y -- %H:%M:%S"):
                info("Initializing a ToolDateTime Widget")
                self.date_time_format = date_time_format
                self.length = 0
                self.string = ""
                self.update()
                ToolbarWidget.__init__(self, self.string, len(self.string))

            def update(self):
                self.string = datetime.now().strftime(self.date_time_format)
                self.length = len(self.string)

        class ToolLabel(ToolbarWidget):
            """A Widget which returns a user defined label"""

            def __init__(self, message=""):
                info("Initializing a ToolLabel Widget")
                ToolbarWidget.__init__(self, message, len(message))

            def update(self):
                pass

    # Now for the Sidebar Widgets

    class SideWidget(Root):
        def __init__(self, height=0):
            info("Initializing the SideWidget class")
            self.height = height

        class SideTodoList(SideWidget):
            def __init__(self, tasks=None):
                info("Initializing a TodoList SideWidget")
                self.tasks = [] if tasks is None else None

                info("Listener?")
                listener = Listener(on_scroll=self.on_scroll)
                listener.start()

            def on_scroll(self, x, y, dx, dy):
                pass

            def update(self):
                pass
