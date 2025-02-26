import re

from aiogram import Router, types

from src.keyboards.subcategories_keyboard import subcategories, get_category_subcategories_keyboard_func

router = Router()


@router.callback_query(lambda c: re.match(r"category_\d+_subcategory_page_\d+$", c.data))
async def handle_page(callback: types.CallbackQuery):
    print(callback.data)
    match = re.match(r"category_(\d+)_subcategory_page_(\d+)", callback.data)
    if match:
        category_id = int(match.group(1))
        page = int(match.group(2))
    else:
        raise Exception(
            f"Invalid callback path: {callback.data}"
        )

    get_subcategories_keyboard = get_category_subcategories_keyboard_func(category_id)
    await callback.message.edit_text(
        "Список подкатегорий:",
        reply_markup=get_subcategories_keyboard(
            page=page,
        ),
    )
    await callback.answer()


@router.callback_query(lambda c: re.match(r"category_\d+_subcategory_\d+$", c.data))
async def handle_subcategory(callback: types.CallbackQuery):
    match = re.match(r"category_(\d+)_subcategory_(\d+)", callback.data)
    if match:
        subcategory_id = int(match.group(2))
    else:
        raise Exception(
            f"Invalid callback path: {callback.data}"
        )

    subcategory = next((s for s in subcategories if s["id"] == subcategory_id), None)
    if subcategory:
        await callback.message.answer(
            f"Вы выбрали: {subcategory['name']}"
        )
    await callback.answer()
