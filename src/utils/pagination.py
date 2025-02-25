from typing import Callable

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_keyboard_with_pagination_func(
        callback_data_prefix: str,
        items: list[dict],
) -> Callable:
    def get_keyboard_with_pagination(
            page: int = 0,
            page_size: int = 3,
    ) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardBuilder()

        start = page * page_size
        end = start + page_size
        paginated_items = items[start:end]

        for item in paginated_items:
            keyboard.add(
                InlineKeyboardButton(
                    text=item["name"],
                    callback_data=f"{callback_data_prefix}_{item['id']}"
                )
            )

        if page > 0:
            keyboard.add(
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data=f"{callback_data_prefix}_page_{page - 1}",
                )
            )

        if end < len(items):
            keyboard.add(
                InlineKeyboardButton(
                    text="Вперед ➡️",
                    callback_data=f"{callback_data_prefix}_page_{page + 1}",
                )
            )

        return keyboard.as_markup()

    return get_keyboard_with_pagination
