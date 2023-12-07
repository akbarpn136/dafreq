import ttkbootstrap as tb

from components.body import DefaultBody
from components.sidebar import DefaultSidebar


class DefaultLayout(tb.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(1, weight=3)

        DefaultSidebar(self)
        DefaultBody(self)
