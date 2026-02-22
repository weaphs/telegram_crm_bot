#bot/handlers/order.py
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from bot.fsm.order_states import OrderStates
from aiogram.types import Message, CallbackQuery, ForceReply
from bot.handlers.client.sign_up import ent_name
from bot.g_services.g_services import google_sheet
from bot.keyboards.reply.order_reply import yes_no_keyboard

router = Router()

@router.callback_query(F.data == 'new_orders', StateFilter(None))
async def check_client(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    if not await google_sheet.check_client_exist(str(user_id)):
        await callback.message.answer("Please Sign Up first!")
        await ent_name(callback, state)
    else:
        await callback.message.answer("Please enter the required number of bottles (1 bottle = 19 liters)")
        await state.set_state(OrderStates.wait_amount)

@router.message(OrderStates.wait_amount)
async def ent_amount(message: Message, state: FSMContext):
    await state.update_data(water_amount=message.text)
    await state.set_state(OrderStates.wait_delivery_time)
    await message.answer("Enter date and time of delivery")

@router.message(OrderStates.wait_delivery_time)
async def ent_amount(message: Message, state: FSMContext):
    await state.update_data(date_time=message.text)
    address = await google_sheet.get_address(str(message.from_user.id))
    if address is not None:
        await state.set_state(OrderStates.wait_address)
        await message.answer(f"Deliver to this address?: '{address}'", reply_markup=yes_no_keyboard())
    else:
        await message.answer("I did`t find any of your addresses. Enter it")
        await dont_have_address(message,state)

@router.message(OrderStates.wait_address, F.text == "Yes")
async def have_address(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id=str(message.from_user.id)
    address = await google_sheet.get_address(user_id)
    amount = data['water_amount']
    date_time = data['date_time']
    if await google_sheet.add_order( user_id,address,amount,date_time):
        await message.answer("Thank you, your order has been accepted.")
    else:
        await message.answer("Sorry, something got wrong... Contact our support!")

@router.message(OrderStates.wait_address, F.text == "No")
async def dont_have_address(message: Message, state: FSMContext):
    await state.set_state(OrderStates.wait_alter_address)
    await message.answer("Enter an address!")

@router.message(OrderStates.wait_alter_address)
async def ent_amount(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = str(message.from_user.id)
    address = message.text
    amount = data['water_amount']
    date_time = data['date_time']
    if await google_sheet.add_order(user_id, address, amount, date_time):
        await message.answer("Thank you, your order has been accepted.")
    else:
        await message.answer("Sorry, something got wrong... Contact our support!")