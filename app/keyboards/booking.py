from datetime import datetime, timedelta

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def get_date_keyboard():
    keyboard = []

    for i in range(3):
        date = datetime.now() + timedelta(days=i)

        date_text = date.strftime("%d.%m")

        keyboard.append(
            [
                InlineKeyboardButton(
                    text=date_text,
                    callback_data=f"date_{date_text}"
                )
            ]
        )

    return InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )


def get_time_keyboard():
    times = [
        "09:00",
        "10:00",
        "11:00",
        "12:00",
        "13:00"
    ]

    keyboard = []

    for time in times:
        keyboard.append(
            [
                InlineKeyboardButton(
                    text=time,
                    callback_data=f"time_{time}"
                )
            ]
        )

    return InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )


def get_confirm_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Подтвердить бронирование ✅",
                    callback_data="confirm_booking"
                )
            ]
        ]
    )


def get_cancel_keyboard(
        bookings
):
    keyboard = []

    for booking_id, date, time in bookings:
        keyboard.append(
            [
                InlineKeyboardButton(
                    text=f"{date} {time} ❌",
                    callback_data=f"cancel_{booking_id}"
                )
            ]
        )

    return InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )