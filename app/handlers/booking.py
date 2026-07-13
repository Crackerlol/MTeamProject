from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from app.database.database import (
    create_booking,
    cancel_booking
)

from app.database.users import get_user_id

from app.keyboards.booking import (
    get_time_keyboard,
    get_confirm_keyboard
)


router = Router()


class BookingState(StatesGroup):
    choosing_date = State()
    choosing_time = State()


@router.callback_query(F.data.startswith("date_"))
async def choose_date(
        callback: CallbackQuery,
        state: FSMContext
):
    date = callback.data.replace(
        "date_",
        ""
    )

    await state.update_data(
        date=date
    )

    await state.set_state(
        BookingState.choosing_time
    )

    await callback.message.edit_text(
        "Выберите время:",
        reply_markup=get_time_keyboard()
    )

    await callback.answer()


@router.callback_query(F.data.startswith("time_"))
async def choose_time(
        callback: CallbackQuery,
        state: FSMContext
):
    time = callback.data.replace(
        "time_",
        ""
    )

    await state.update_data(
        time=time
    )

    data = await state.get_data()

    await callback.message.edit_text(
        f"Дата: {data['date']}\n"
        f"Время: {time}\n\n"
        "Подтвердите бронирование:",
        reply_markup=get_confirm_keyboard()
    )

    await callback.answer()


@router.callback_query(
    F.data == "confirm_booking"
)
async def confirm_booking(
        callback: CallbackQuery,
        state: FSMContext
):
    data = await state.get_data()

    user_id = await get_user_id(
        callback.from_user.id
    )

    result = await create_booking(
        user_id=user_id,
        date=data["date"],
        time=data["time"]
    )

    if result:
        await callback.message.edit_text(
            "✅ Бронирование успешно создано!"
        )

    else:
        await callback.message.edit_text(
            "❌ Это время уже занято."
        )

    await state.clear()
    await callback.answer()


@router.callback_query(
    F.data.startswith("cancel_")
)
async def cancel_user_booking(
        callback: CallbackQuery
):
    booking_id = int(
        callback.data.replace(
            "cancel_",
            ""
        )
    )

    user_id = await get_user_id(
        callback.from_user.id
    )

    await cancel_booking(
        booking_id,
        user_id
    )

    await callback.message.edit_text(
        "✅ Бронирование отменено."
    )

    await callback.answer()