from telegram import Update
from telegram.ext import CallbackContext
from app.quotes import get_random_quote
from app.keyboards import main_keyboard

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Привіт! Я бот, що надсилає цитати.", reply_markup=main_keyboard())

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Я можу надсилати випадкові цитати. Використай /quote.")

async def quote_command(update: Update, context: CallbackContext):
    quote = get_random_quote()
    await update.message.reply_text(quote)
