from app.keyboards.main_menu import main_keyboard
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.database.users import add_user

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):

    await add_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        full_name=message.from_user.full_name
    )

    await message.answer(
        "Привет! 👋\n\n"
        "Молодец, что нашел время для учебы 📖 \n"
        "Давай забронируем место ✅ ",
        reply_markup = main_keyboard
    )