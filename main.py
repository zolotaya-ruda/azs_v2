import asyncio
import tornado.web

import settings
from handlers import MainPageHandler


async def main():
    application = tornado.web.Application(**settings.app_settings)
    application.add_handlers(r'.*', [
        (r"/", MainPageHandler),
    ])

    application.listen(8000)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
