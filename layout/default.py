import asyncio
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from async_tkinter_loop import async_handler


class DefaultLayout(tb.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.progressbar = tb.Progressbar(self, length=280, mode="determinate")
        self.progressbar.pack(side=TOP, padx=5, pady=10)

        b1 = tb.Button(
            self,
            text="Calculate Sync",
            bootstyle=SUCCESS,
            command=self.calculate_sync
        )
        b1.pack(side=LEFT, padx=5, pady=10)

        b2 = tb.Button(
            self,
            text="Calculate Async",
            bootstyle=(INFO, OUTLINE),
            command=async_handler(self.calculate_async)
        )
        b2.pack(side=LEFT, padx=5, pady=10)

        self.place_window_center()

    def calculate_sync(self):
        max = 3000000
        for i in range(1, max):
            self.progressbar["value"] = i / max * 100

    async def calculate_async(self):
        max = 3000000
        for i in range(1, max):
            self.progressbar["value"] = i / max * 100
            if i % 1000 == 0:
                await asyncio.sleep(0)
