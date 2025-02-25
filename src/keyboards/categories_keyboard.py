from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from src.utils.pagination import get_keyboard_with_pagination_func

categories = [
    {"id": 1, "name": "Товар 1"},
    {"id": 2, "name": "Товар 2"},
    {"id": 3, "name": "Товар 3"},
    {"id": 4, "name": "Товар 4"},
    {"id": 5, "name": "Товар 5"},
    {"id": 6, "name": "Товар 6"},
    {"id": 7, "name": "Товар 7"},
    {"id": 8, "name": "Товар 8"},
    {"id": 9, "name": "Товар 9"},
    {"id": 10, "name": "Товар 10"},
]


# def get_categories_keyboard(
#         page: int = 0,
#         page_size: int = 3,
# ):
#     keyboard = InlineKeyboardBuilder()
#
#     start = page * page_size
#     end = start + page_size
#     paginated_categories = categories[start:end]
#
#     for category in paginated_categories:
#         keyboard.add(
#             InlineKeyboardButton(
#                 text=category["name"],
#                 callback_data=f"category_{category['id']}"
#             )
#         )
#
#     if page > 0:
#         keyboard.add(
#             InlineKeyboardButton(
#                 text="⬅️ Назад",
#                 callback_data=f"category_page_{page - 1}",
#             )
#         )
#
#     if end < len(categories):
#         keyboard.add(
#             InlineKeyboardButton(
#                 text="Вперед ➡️",
#                 callback_data=f"category_page_{page + 1}",
#             )
#         )
#
#     return keyboard.as_markup()


get_categories_keyboard = get_keyboard_with_pagination_func(
    callback_data_prefix="category",
    items=categories,
)
