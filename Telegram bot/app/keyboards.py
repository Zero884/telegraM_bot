from telegram import ReplyKeyboardMarkup

def main_keyboard():
    return ReplyKeyboardMarkup([ 
        ["Отримати цитату"], 
        ["Інші функції"]  
    ], resize_keyboard=True)