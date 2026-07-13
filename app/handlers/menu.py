from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.booking import (
    get_date_keyboard,
    get_cancel_keyboard
)

from app.database.users import get_user_id
from app.database.database import get_user_bookings


router = Router()


@router.message(F.text == "Забронировать место 📚")
async def booking(message: Message):
    await message.answer(
        "Выбери дату:",
        reply_markup=get_date_keyboard()
    )


@router.message(F.text == "Мои бронирования 📖")
async def my_bookings(message: Message):
    user_id = await get_user_id(
        message.from_user.id
    )

    bookings = await get_user_bookings(
        user_id
    )

    if not bookings:
        await message.answer(
            "У вас нет бронирований."
        )
        return

    await message.answer(
        "Ваши бронирования:",
        reply_markup=get_cancel_keyboard(
            bookings
        )
    )


@router.message(F.text == "Помощь ℹ️")
async def help_command(message: Message):
    await message.answer(
        "Если возникли вопросы, обратись к администратору."
    )