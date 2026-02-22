#bot/handlers/start.py
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.keyboards.inline.main_menu import main_menu_keyboard
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command("start"))
async def cmd_start(message:Message, state: FSMContext):
    await state.clear()
    name = message.from_user.full_name
    await message.answer(f"👋 Hello! Would you like some water?👇.",
                         reply_markup= main_menu_keyboard())
