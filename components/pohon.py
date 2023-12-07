import os
from pathlib import Path
import ttkbootstrap as tb
from ttkbootstrap.constants import *


class PohonComponent:
    def __init__(self, container, path=None):
        self.container = container
        self.path = path

        if self.path is None:
            dirs = Path.home()
        else:
            dirs = os.listdir(self.path)

        print(dirs)

        tree = tb.Treeview(self.container, height=15)
        tree.heading('#0', text="Data getaran", anchor=NW)
        tree.insert('', END, text='Administration', iid=0, open=False)
        tree.grid(column=0, row=1, pady=5, sticky=NW, columnspan=2)
