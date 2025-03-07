from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def main_keyboard():
    keyboard = [
        [KeyboardButton(text="Отримати цитату")],
        [KeyboardButton(text="Інші функції")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
