from aiogram import F, Router, types


router = Router()


@router.callback_query(F.data == "mock")
async def handle_catalog(callback: types.CallbackQuery):
    await callback.message.answer("Это новое сообщение в чате!")
    await callback.answer()
