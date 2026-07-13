from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.keyboards.booking import get_time_keyboard

router = Router()

@router.callback_query(F.data.startswith("date_"))
async def choose_date(callback: CallbackQuery):
    selected_date = callback.data.replace("date_", "")

    await callback.message.edit_text(
        f"Вы выбрали дату: {selected_date}\n\n"
        "Теперь выберите время:",
        reply_markup=get_time_keyboard()
    )

    await callback.answer()

@router.callback_query(F.data.startswith("time_"))
async def choose_time(callback: CallbackQuery):
    selected_time = callback.data.replace("time_", "")

    await callback.message.edit_text(
        f"Вы выбрали время: {selected_time}\n\n"
        "Нажмите кнопку ниже для подтверждения бронирования."
    )

    await callback.answer()