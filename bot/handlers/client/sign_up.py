#bot/handlers/sign_up.py
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from bot.fsm.sign_up_states import SignUpStates
from aiogram.types import Message, CallbackQuery, ForceReply
from bot.handlers.client.start import cmd_start
from bot.g_services.g_services import google_sheet

router = Router()

@router.callback_query(F.data == 'register', StateFilter(None))
async def ent_name(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("What is your full name?", reply_markup=ForceReply(input_field_placeholder="Put here your full name..."))
    await state.set_state(SignUpStates.wait_full_name)

@router.message(SignUpStates.wait_full_name)
async def ent_phone(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer(f"Please enter your phone number", reply_markup=ForceReply(input_field_placeholder="Put here your phone number..."))
    await state.set_state(SignUpStates.wait_phone)

@router.message(SignUpStates.wait_phone)
async def ent_address(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer(f"Please provide the delivery address.", reply_markup=ForceReply(input_field_placeholder="Put here address..."))
    await state.set_state(SignUpStates.wait_address)

@router.message(SignUpStates.wait_address)
async def end_reg(message: Message, state: FSMContext):
    await state.update_data(address=message.text, user_id=message.from_user.id)
    await google_sheet.add_client(await state.get_data())
    await state.clear()
    await message.answer(f"Thank you for registration!.")
    await cmd_start(message)
