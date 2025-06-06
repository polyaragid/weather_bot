from config.settings_bot import bot_config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from routers import commands , weather, favorites, support
from middlewares.throttling import AdvancedAntiSpamMiddleware
from utils import logger
import asyncio



async def main():
    bot = Bot(token=bot_config.telegram_api_key)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Регистрация роутеров
    dp.include_router(commands.router)
    dp.include_router(weather.router)
    dp.include_router(favorites.router)
    dp.include_router(support.router)

    # Подключение с настройками: 3 сообщения в 5 секунд, бан на 5 минут
    #dp.message.middleware(AdvancedAntiSpamMiddleware(limit=3, interval=5, ban_time=300))
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


