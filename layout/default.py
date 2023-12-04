import ttkbootstrap as tb
from ttkbootstrap.constants import *


class DefaultLayout(tb.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        b1 = tb.Button(self, text="Button 1", bootstyle=SUCCESS)
        b1.pack(side=LEFT, padx=5, pady=10)

        b2 = tb.Button(self, text="Button 2", bootstyle=(INFO, OUTLINE))
        b2.pack(side=LEFT, padx=5, pady=10)

        self.title = "DaFreq LA3"
