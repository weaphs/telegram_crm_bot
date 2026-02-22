#bot/handlers/my_profile.py
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from bot.fsm.order_states import OrderStates
from aiogram.types import Message, CallbackQuery, ForceReply
from bot.handlers.client.sign_up import ent_name
from bot.g_services.g_services import google_sheet
from bot.keyboards.reply.order_reply import yes_no_keyboard

router = Router()

@router.callback_query(F.data == 'my_orders')
async def check_orders(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    data = await google_sheet.my_orders(str(user_id))
    if data:
        await callback.message.answer("Your orders:\n\n")
        for row in data:
            await callback.message.answer(f"Address: {row[2]}\nBottle amount: {row[3]}\nDate and time of delivery: {row[4]}")
        await callback.message.answer("To cancel order contact our manager.")
    else:
        await callback.message.answer("You don`t have any orders")
