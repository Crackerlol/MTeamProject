from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Забронировать место 📚")
        ],
        [
            KeyboardButton(text="Мои бронирования 📖")
        ],
        [
            KeyboardButton(text="Помощь ℹ️")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что будем делать ?"
)