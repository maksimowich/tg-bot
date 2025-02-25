from aiogram import Router, types

from src.keyboards.categories_keyboard import categories, get_categories_keyboard

router = Router()


@router.callback_query(lambda c: c.data.startswith("category_page_"))
async def handle_page(callback: types.CallbackQuery):
    page = int(callback.data.split("_")[-1])
    await callback.message.edit_text(
        "Список категорий:",
        reply_markup=get_categories_keyboard(page=page),
    )
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("category_"))
async def handle_category(callback: types.CallbackQuery):
    category_id = int(callback.data.split("_")[-1])
    category = next((c for c in categories if c["id"] == category_id), None)
    if category:
        await callback.message.answer(f"Вы выбрали: {category['name']}")
    await callback.answer()
