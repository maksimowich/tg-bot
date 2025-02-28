from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.ext.asyncio import AsyncSession

from src.handlers.cart import router
from src.services import CartService


@router.callback_query(lambda c: c.data == "view_cart")
async def view_cart(
        callback: types.CallbackQuery,
        session: AsyncSession,
):
    user_id = callback.from_user.id

    cart_items = await CartService.get_cart_items(
        session=session,
        user_id=str(user_id),
    )

    if not cart_items:
        await callback.message.answer("Ваша корзина пуста.")

    else:
        text = "Ваша корзина:\n\n"
        builder = InlineKeyboardBuilder()

        for cart_item in cart_items:
            text += f"📦 Товар {cart_item.product_id} — {cart_item.quantity} шт.\n"
            builder.button(
                text=f"❌ Удалить товар {cart_item.product_id}",
                callback_data=f"remove_from_cart_{cart_item.id}",
            )

        builder.button(
            text="Очистить корзину",
            callback_data="clear_cart",
        )

        builder.button(
            text="️Сделать заказ",
            callback_data="make_order",
        )

        await callback.message.answer(
            text,
            reply_markup=builder.as_markup(),
        )
        await callback.answer()
