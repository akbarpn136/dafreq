import ttkbootstrap as tb
from ttkbootstrap.constants import *

from components.cari import CariComponent
from components.pohon import PohonComponent


class DefaultSidebar:
    def __init__(self, container):
        self.container = container

        sidebar = tb.Frame(self.container)
        sidebar.grid(column=0, row=0, padx=3, pady=3, sticky=NW)

        PohonComponent(sidebar)
        CariComponent(sidebar)
