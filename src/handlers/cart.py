from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


class CartState(StatesGroup):
    waiting_for_quantity = State()
    waiting_for_confirmation = State()


@router.callback_query(lambda c: c.data.startswith("add_to_cart_product_"))
async def add_to_cart(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    product_id = int(callback.data.split("_")[-1])

    await state.update_data(product_id=product_id)
    await state.set_state(CartState.waiting_for_quantity)

    await callback.message.answer(
        f"Товар {product_id} добавлен в корзину. Введите количество:"
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "view_cart")
async def view_cart(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    data = await state.get_data()
    cart = data.get("cart", [])

    if not cart:
        await callback.message.answer("Ваша корзина пуста.")

    else:
        text = "Ваша корзина:\n\n"
        builder = InlineKeyboardBuilder()

        for item in cart:
            text += f"📦 Товар {item['product_id']} — {item['quantity']} шт.\n"
            builder.button(
                text=f"❌ Удалить товар {item['product_id']}",
                callback_data=f"remove_from_cart_{item['product_id']}",
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


@router.callback_query(lambda c: c.data.startswith("remove_from_cart_"))
async def remove_from_cart(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    product_id = int(callback.data.split("_")[-1])
    data = await state.get_data()
    cart = data.get("cart", [])

    cart = [item for item in cart if item["product_id"] != product_id]

    await state.update_data(cart=cart)

    await callback.message.delete()

    await callback.message.answer(f"Товар {product_id} удалён из корзины!")
    await view_cart(callback, state)


@router.callback_query(lambda c: c.data == "clear_cart")
async def clear_cart(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    await state.update_data(cart=[])

    await callback.message.delete()

    await callback.message.answer("Корзина очищена.")
    await view_cart(callback, state)


@router.message(CartState.waiting_for_quantity)
async def process_quantity(
        message: types.Message,
        state: FSMContext,
):
    data = await state.get_data()
    cart = data.get("cart", [])
    product_id = data.get("product_id")

    try:
        quantity = int(message.text)
        if quantity <= 0:
            await message.answer("Количество должно быть больше 0.")
            return
    except ValueError:
        await message.answer("Пожалуйста, введите число.")
        return

    for item in cart:
        if item["product_id"] == product_id:
            item["quantity"] = quantity
            break

    await state.update_data(quantity=quantity)
    await state.set_state(CartState.waiting_for_confirmation)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Да", callback_data="confirm_add"),
            InlineKeyboardButton(text="❌ Нет", callback_data="cancel_add"),
        ]
    ])

    await message.answer(
        f"Вы хотите добавить товар {product_id} в количестве {quantity} шт. в корзину?",
        reply_markup=keyboard,
    )


@router.callback_query(CartState.waiting_for_confirmation, lambda c: c.data == "confirm_add")
async def confirm_add(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    data = await state.get_data()
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    cart = data.get("cart", [])

    cart.append({"product_id": product_id, "quantity": quantity})

    await state.update_data(cart=cart)

    await callback.message.delete()
    await callback.message.answer(f"Товар {product_id} в количестве {quantity} шт. добавлен в корзину!")
    await callback.answer()


@router.callback_query(CartState.waiting_for_confirmation, lambda c: c.data == "cancel_add")
async def cancel_add(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    await state.clear()
    await callback.message.delete()
    await callback.message.answer("Добавление товара отменено.")
    await callback.answer()

