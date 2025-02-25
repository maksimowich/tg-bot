from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.keyboards.start_keyboard import get_start_keyboard


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await show_start_keyboard(message)


async def show_start_keyboard(message: types.Message):
    await message.answer(
        "Выберите действие:",
        reply_markup=get_start_keyboard(),
    )


@router.callback_query(F.data == "catalog")
async def handle_catalog(callback: types.CallbackQuery):
    await callback.message.answer("Это новое сообщение в чате!")
    await callback.answer()


