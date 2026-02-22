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

@router.callback_query(F.data == 'profile')
async def check_client(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    data = await google_sheet.get_profile(str(user_id))
    if data:
        await callback.message.answer(f"Full name: {data[0]}\nPhone number: {data[1]}\nAddress: {data[2]} ")
    else:
        await callback.message.answer("You don`t have profile! Please sign up first!")
