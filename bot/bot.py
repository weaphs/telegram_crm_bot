#bot/bot.py
from aiogram import Bot, Dispatcher
from bot.handlers.client import start, sign_up, order, my_profile, my_orders, donate
from aiogram.fsm.storage.memory import MemoryStorage
from settings.settings import settings
from bot.middlewares.block_middleware import BlackListMiddleware
from bot.g_services.g_services import google_sheet

bot = Bot(settings.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.update.outer_middleware(BlackListMiddleware(google_sheet))
dp.include_router(start.router)
dp.include_router(sign_up.router)
dp.include_router(order.router)
dp.include_router(my_profile.router)
dp.include_router(my_orders.router)
dp.include_router(donate.invoices_router)

