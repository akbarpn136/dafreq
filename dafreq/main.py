import asyncio
from layout.default import DefaultLayout


def run():
    app = DefaultLayout(
        title="DaFreq LA3",
        themename="darkly",
        iconphoto="logo.png",
        minsize=(800, 600),
        loop=asyncio.get_event_loop()
    )

    asyncio.run(app.show())
