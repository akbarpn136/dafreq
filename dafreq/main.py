from async_tkinter_loop import async_mainloop

from layout.default import DefaultLayout


def run():
    app = DefaultLayout(
        title="DaFreq LA3",
        themename="darkly",
        iconphoto="logo.png",
        minsize=(800, 600),
    )

    async_mainloop(app)
