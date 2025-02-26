from typing import Callable

from src.utils.pagination import get_keyboard_with_pagination_func

subcategories = [
    {"id": 1, "category_id": 1, "name": "Подкатегория 1"},
    {"id": 2, "category_id": 1, "name": "Подкатегория 2"},
    {"id": 3, "category_id": 1, "name": "Подкатегория 3"},
    {"id": 4, "category_id": 1, "name": "Подкатегория 4"},
    {"id": 5, "category_id": 1, "name": "Подкатегория 5"},
    {"id": 6, "category_id": 1, "name": "Подкатегория 6"},
    {"id": 7, "category_id": 1, "name": "Подкатегория 7"},
    {"id": 8, "category_id": 1, "name": "Подкатегория 8"},
    {"id": 9, "category_id": 2, "name": "Подкатегория 9"},
    {"id": 10, "category_id": 2, "name": "Подкатегория 10"},
]


def get_category_subcategories(
        category_id: int,
) -> list[dict]:
    return [
        subcategory for subcategory in subcategories
        if subcategory["category_id"] == category_id
    ]


def get_category_subcategories_keyboard_func(
        category_id: int,
) -> Callable:
    category_subcategories = get_category_subcategories(category_id)

    get_subcategories_keyboard = get_keyboard_with_pagination_func(
        callback_data_prefix=f"category_{category_id}_subcategory",
        items=category_subcategories,
    )
    return get_subcategories_keyboard
