#bot/handlers/donate.py
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery


invoices_router = Router(name=__name__)

donates_activated = True

@invoices_router.callback_query(F.data == 'donate_star')
async def donate(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer_invoice(
        title="DONATING 1 STAR",
        description="Confirm your intention!",
        prices=[
            LabeledPrice(label="Your donate!", amount=1)
        ],
        payload="demo",
        currency="XTR",
    )

@invoices_router.pre_checkout_query(F.invoice_payload == "demo")
async def pre_checkout_query(query: PreCheckoutQuery) -> None:
    if donates_activated:
        await query.answer(ok=True)
    else:
        await query.answer(ok=False, error_message="Donates are disabled")

# AUTOMATIC REFUNDING FOR DEMO VERSION
@invoices_router.message(F.successful_payment)
async def successful_payment(message: Message, bot: Bot) -> None:
    await bot.refund_star_payment(
        user_id=message.from_user.id,
        telegram_payment_charge_id=message.successful_payment.telegram_payment_charge_id,
    )
    await message.answer("Thanks. Your payment has been refunded.")