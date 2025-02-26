from src.utils.pagination import get_keyboard_with_pagination_func

categories = [
    {"id": 1, "name": "Категория 1"},
    {"id": 2, "name": "Категория 2"},
    {"id": 3, "name": "Категория 3"},
    {"id": 4, "name": "Категория 4"},
    {"id": 5, "name": "Категория 5"},
    {"id": 6, "name": "Категория 6"},
    {"id": 7, "name": "Категория 7"},
    {"id": 8, "name": "Категория 8"},
    {"id": 9, "name": "Категория 9"},
    {"id": 10, "name": "Категория 10"},
]


get_categories_keyboard = get_keyboard_with_pagination_func(
    callback_data_prefix="category",
    items=categories,
)
