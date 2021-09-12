from datetime import datetime
from Root_Class import Root


class Widget(Root):
    """Organizational class for widgets"""

    def __init__(self, string: str, length: int):
        self.string = string
        self.length = length
        
        Root.__init__(self)


class Date_Time(Widget):
    """A widget that returns a string of the current date and time in the specified format"""

    def __init__(self, date_time_format="%B %d, %Y -- %H:%M:%S"):
        self.date_time_format = date_time_format
        self.length = 0
        self.string = ""
        self.update()
        Widget.__init__(self, self.string, len(self.string))

    def update(self):
        self.string = datetime.now().strftime(self.date_time_format)
        self.length = len(self.string)


class Label(Widget):
    """A Widget which returns a user defined label"""
    def __init__(self, message=""):
        Widget.__init__(self, message, len(message))

    def update(self):
        pass
