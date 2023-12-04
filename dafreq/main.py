from layout.default import DefaultLayout


def run():
    app = DefaultLayout(
        title="DaFreq LA3",
        themename="darkly",
        iconphoto="logo.png",
        minsize=(800, 600),
    )

    app.place_window_center()
    app.mainloop()
