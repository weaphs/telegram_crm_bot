#bot/middlewares/block_middleware.py
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from aiogram.types import TelegramObject

class BlackListMiddleware(BaseMiddleware):

    def __init__(self, google_sheet):
        self.google_sheet = google_sheet

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        user = data.get("event_from_user")

        if user:
            is_blocked = await self.google_sheet.check_blacklist(str(user.id))

            if is_blocked:
                if hasattr(event, "answer"):
                    await event.answer("You are blocked.")
                return

        return await handler(event, data)