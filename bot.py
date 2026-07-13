import asyncio
from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from app.handlers.start import router as start_router
from app.handlers.menu import router as menu_router
from app.database.database import create_database
from app.handlers.booking import router as booking_router

async def main():
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(booking_router)

    await create_database()

    print("Бот запущен 🚀")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())