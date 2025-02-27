from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


router = Router()


class OrderStates(StatesGroup):
    waiting_for_address = State()


@router.callback_query(lambda c: c.data == 'make_order')
async def process_make_order(
        callback_query: types.CallbackQuery,
        state: FSMContext,
):
    await callback_query.message.answer("Введите адрес для доставки:")
    await state.set_state(OrderStates.waiting_for_address)


@router.message(OrderStates.waiting_for_address)
async def process_address(
        message: types.Message,
        state: FSMContext,
):
    address = message.text
    await state.update_data(address=address)

    payment_link = create_payment(address)

    await message.answer(
        f"Ваш заказ по адресу {address} оформлен. "
        f"Ссылка для оплаты: {payment_link}")
    await state.clear()


def create_payment(address):
    return "https://payment.link/example"
