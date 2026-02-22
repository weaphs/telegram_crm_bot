#bot/keyboards/inline/main_menu
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard ():
    row_1 = [
        InlineKeyboardButton(text="Sign Up", callback_data="register"),
        InlineKeyboardButton(text="My Profile", callback_data="profile")]
    row_2 =[
        InlineKeyboardButton(text="Order a Water", callback_data="new_orders"),
        InlineKeyboardButton(text="My orders", callback_data="my_orders")]
    row_3 = [
        InlineKeyboardButton(text="Support with a Star ⭐", callback_data="donate_star")]

    main_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[row_1,row_2,row_3])
    return main_menu_keyboard