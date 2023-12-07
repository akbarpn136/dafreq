import ttkbootstrap as tb
from ttkbootstrap.constants import *

from components.cari import CariComponent


class DefaultSidebar:
    def __init__(self, container):
        self.container = container

        sidebar = tb.Frame(self.container)
        sidebar.grid(column=0, row=0, padx=3, pady=3, sticky=NW)

        CariComponent(sidebar)
