from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from components.pohon import PohonComponent


class CariComponent:
    def __init__(self, container):
        self.container = container
        self.path = tb.Entry(self.container, bootstyle="primary", width=26)
        self.path.grid(column=0, row=0, sticky=NW)

        tb.Button(self.container, bootstyle="primary",
                  text="", command=self.opendir).grid(column=1, row=0, sticky=NW)

    def opendir(self):
        dir = filedialog.askdirectory()

        self.path.delete(0, END)
        self.path.insert(0, dir)

    def get_path(self):
        return self.path.get()
