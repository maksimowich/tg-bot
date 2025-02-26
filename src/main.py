from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import start, category, subcategory
from src.core.config import app_settings


async def main():
    bot = Bot(
        token=app_settings.tg.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(
        storage=MemoryStorage(),
    )

    dp.include_router(start.router)
    dp.include_router(category.router)
    dp.include_router(subcategory.router)

    await bot.delete_webhook()
    await bot.session.close()

    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
