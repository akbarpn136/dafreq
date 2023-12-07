import ttkbootstrap as tb
from ttkbootstrap.constants import *


class DefaultBody:
    def __init__(self, container):
        self.container = container

        body = tb.Frame(self.container)
        body.grid(column=1, row=0, ipadx=3, ipady=3, sticky=NW)
        tb.Label(body, text="INFO 1").grid(column=0, row=0)
        tb.Label(body, text="INFO 2").grid(column=0, row=1)
        tb.Label(body, text="INFO 3").grid(column=0, row=2)