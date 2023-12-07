from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *


class CariComponent:
    def __init__(self, container):
        self.path = tb.Entry(container, bootstyle="primary", width=30)
        self.path.grid(column=0, row=0)

        tb.Button(container, bootstyle="primary",
                  text="", command=self.opendir).grid(column=1, row=0)

    def opendir(self):
        dir = filedialog.askdirectory()

        self.path.delete(0, END)
        self.path.insert(0, dir)

    def get_path(self):
        return self.path.get()
