from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.keyboards.products_keyboard import show_products

router = Router()


@router.callback_query(lambda c: c.data == "prev_products_page")
async def prev_products_page(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    data = await state.get_data()
    current_page = data.get("current_page", 0)

    if current_page > 0:
        await state.update_data(current_page=current_page - 1)
        await show_products(callback.message, state)
    await callback.answer()


@router.callback_query(lambda c: c.data == "next_products_page")
async def next_products_page(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    data = await state.get_data()
    current_page = data.get("current_page", 0)

    await state.update_data(current_page=current_page + 1)
    await show_products(callback.message, state)
    await callback.answer()
