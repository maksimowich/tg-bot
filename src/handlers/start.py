from aiogram import Bot, Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.core.config import app_settings
from src.core.is_subcribed import is_subscribed
from src.keyboards.start_keyboard import get_start_keyboard


router = Router()


@router.message(Command("start"))
async def cmd_start(
        message: types.Message,
        bot: Bot,
):
    user_id = message.from_user.id

    if not await is_subscribed(bot, user_id):
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Подписаться на канал",
            url=f"https://t.me/{app_settings.tg.channel_id[1:]}"
        ))
        await message.answer(
            "Пожалуйста, подпишитесь на канал для использования бота.",
            reply_markup=builder.as_markup()
        )
    else:
        await show_start_keyboard(message)


async def show_start_keyboard(message: types.Message):
    await message.answer(
        "Выберите действие:",
        reply_markup=get_start_keyboard(),
    )
