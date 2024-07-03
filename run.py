from aiogram import Bot, Dispatcher

import asyncio
import logging
import sys

from config import TOKEN
from app.handlers import router
from app.database.models import create_tables


async def main() -> None:
    await create_tables()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
