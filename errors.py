class Error(Exception):
    pass


class TerminalTooThinError(Error):
    """Exception raised for terminals which are too thin to support TelviK."""
    def __init__(self, width: int, min_width: int, message="Terminal is too thin to support TelviK."):
        self.width = width
        self.min_width = min_width
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"A width of {self.width} columns is less than {self.min_width}"


class TerminalTooShortError(Error):
    """Exception raised when terminals are shorter than the minimum height to support TelviK"""
    def __init__(self, height: int, min_height: int, message="Terminal is too short to support TelviK."):
        self.height = height
        self.min_height = min_height
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"A height of {self.height} lines is less than {self.min_height}"


# TODO - Make this error obsolete
class TodoTooLongError(Error):
    """Exception raised when a todo list is too big """
    def __init__(self, list_len: int, max_len: int):
        self.list_len = list_len
        self.max_len = max_len

    def __str__(self):
        return f"{self.list_len} is larger than {self.max_len}"


# TODO - Make this error obsolete
class ItemTooLongError(Error):
    """Exception raised when a todo list is too big """
    def __init__(self, item_len: int, max_len: int):
        self.item_len = item_len
        self.max_len = max_len

    def __str__(self):
        return f"{self.item_len} is larger than {self.max_len}"
