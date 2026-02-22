from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def yes_no_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Yes"),
                KeyboardButton(text="No"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return keyboard
