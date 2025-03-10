from aiogram import types, Router
from aiogram.filters import Command, CommandStart
from app.database import get_random_quote
from app.keyboards import main_keyboard

router = Router()

@router.message(CommandStart()) 
async def start_command(message: types.Message):
    await message.answer("Привіт! Я бот, що надсилає цитати.", reply_markup=await main_keyboard())

@router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Я можу надсилати випадкові цитати. Використай /quote.")

@router.message(Command("quote"))
async def quote_command(message: types.Message):
    quote = get_random_quote()
    await message.answer(quote)

@router.message()
async def handle_buttons(message: types.Message):
    if message.text == "Отримати цитату":
        quote = get_random_quote()
        await message.answer(quote)
    elif message.text == "Інші функції":
        await message.answer("Поки що інших функцій немає.")
