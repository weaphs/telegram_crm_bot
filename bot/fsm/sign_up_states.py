#bot/fsm/sign_up_states.py
from aiogram.fsm.state import State, StatesGroup

class SignUpStates(StatesGroup):
    wait_full_name = State()
    wait_phone = State()
    wait_address = State()
