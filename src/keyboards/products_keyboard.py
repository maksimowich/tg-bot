from aiogram import types
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.input_file import FSInputFile

PAGE_SIZE = 3


async def show_products(
        message: types.Message,
        state: FSMContext,
):
    products = [
        {"id": 1, "name": "Товар 1", "price": 100, "photo": "../xxx.jpg"},
        {"id": 2, "name": "Товар 2", "price": 200, "photo": "../xxx.jpg"},
        {"id": 3, "name": "Товар 3", "price": 200, "photo": "../xxx.jpg"},
        {"id": 4, "name": "Товар 4", "price": 200, "photo": "../xxx.jpg"},
        {"id": 5, "name": "Товар 5", "price": 200, "photo": "../xxx.jpg"},
        {"id": 6, "name": "Товар 6", "price": 200, "photo": "../xxx.jpg"},
        {"id": 7, "name": "Товар 7", "price": 200, "photo": "../xxx.jpg"},
        {"id": 8, "name": "Товар 8", "price": 200, "photo": "../xxx.jpg"},
        {"id": 9, "name": "Товар 9", "price": 200, "photo": "../xxx.jpg"},
        {"id": 10, "name": "Товар 10", "price": 200, "photo": "../xxx.jpg"},
    ]

    data = await state.get_data()
    current_page = data.get("current_page", 0)

    start = current_page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_products = products[start:end]

    for product in page_products:
        text = f"📦 {product['name']}\n💰 {product['price']} руб."
        builder = InlineKeyboardBuilder()
        builder.button(
            text="🛒 Положить в корзину",
            callback_data=f"add_to_cart_product_{product['id']}",
        )
        await message.answer_photo(
            photo=FSInputFile(product["photo"]),
            caption=text,
            reply_markup=builder.as_markup()
        )

    builder = InlineKeyboardBuilder()
    if current_page > 0:
        builder.button(
            text="⬅️ Назад",
            callback_data="prev_products_page",
        )
    if end < len(products):
        builder.button(
            text="Вперёд ➡️",
            callback_data="next_products_page",
        )

    total_pages = (
        (len(products) // PAGE_SIZE) + (1 if len(products) % PAGE_SIZE != 0 else 0)
    )
    await message.answer(
        f"Страница {current_page + 1} из {total_pages}. Выберите товар:",
        reply_markup=builder.as_markup(),
    )
