import ttkbootstrap as tb
from ttkbootstrap.constants import *


class DefaultSidebar:
    def __init__(self, container):
        self.container = container

        sidebar = tb.Frame(self.container)
        sidebar.grid(column=0, row=0, ipadx=3, ipady=3, sticky=NW)
        tb.Label(sidebar, text="INFO 1").grid(column=0, row=0)
        tb.Label(sidebar, text="INFO 2").grid(column=1, row=0)
        tb.Label(sidebar, text="INFO 3").grid(column=2, row=0)