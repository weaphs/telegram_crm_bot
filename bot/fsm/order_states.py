#bot/fsm/order_states.py
from aiogram.fsm.state import State, StatesGroup

class OrderStates(StatesGroup):
    wait_amount = State()
    wait_address = State()
    wait_alter_address = State()
    wait_delivery_time = State()

