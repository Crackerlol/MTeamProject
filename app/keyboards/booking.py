from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_date_keyboard():
    dates = [
        ("12 июля", "date_12"),
        ("13 июля", "date_13"),
        ("14 июля", "date_14"),
    ]

    keyboard = []

    for text, callback in dates:
        keyboard.append([
            InlineKeyboardButton(
                text=text,
                callback_data=callback
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


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
        keyboard.append([
            InlineKeyboardButton(
                text=time,
                callback_data=f"time_{time}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)