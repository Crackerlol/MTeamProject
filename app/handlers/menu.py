from aiogram import Router, F
from aiogram.types import Message
from app.keyboards.booking import get_date_keyboard

router = Router()


@router.message(F.text == "Забронировать место 📚")
async def booking(message: Message):
    await message.answer(
        "Выбери дату:",
        reply_markup=get_date_keyboard()
    )


@router.message(F.text == "Помощь ℹ️")
async def help_command(message: Message):
    await message.answer(
        "Если возникли вопросы, обратись к администратору."
    )