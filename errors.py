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
