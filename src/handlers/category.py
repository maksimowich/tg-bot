import re

from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from loguru import logger

from src.keyboards.categories_keyboard import categories, get_categories_keyboard
from src.keyboards.subcategories_keyboard import get_category_subcategories_keyboard_func


router = Router()


@router.callback_query(lambda c: re.match(r"category_page_\d+$", c.data))
async def handle_page(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    page = int(callback.data.split("_")[-1])
    data = await state.get_data()
    first_opened = data.get("first_opened", True)

    if first_opened:
        await callback.message.answer(
            "Список категорий:",
            reply_markup=get_categories_keyboard(page=page),
        )
        await state.update_data(first_opened=False)
    else:
        await callback.message.edit_text(
            "Список категорий:",
            reply_markup=get_categories_keyboard(page=page),
        )
        await callback.answer()


@router.callback_query(lambda c: re.match(r"category_\d+$", c.data))
async def handle_category(callback: types.CallbackQuery):
    logger.info(callback.data)
    category_id = int(callback.data.split("_")[-1])
    category = next((c for c in categories if c["id"] == category_id), None)
    if category:
        get_subcategories_keyboard = get_category_subcategories_keyboard_func(category["id"])
        await callback.message.answer(
            "Выберите подкатегорию:",
            reply_markup=get_subcategories_keyboard(page=0),
        )
    await callback.answer()
