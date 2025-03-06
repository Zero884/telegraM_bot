import os
import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.quotes import get_random_quote

CHAT_ID = os.getenv("CHAT_ID")

def schedule_daily_quote(app):
    async def send_daily_quote():
        if not CHAT_ID:
            print("CHAT_ID не встановлено. Не можу відправити цитату.")
            return
        quote = get_random_quote()
        await app.bot.send_message(chat_id=CHAT_ID, text=quote)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_daily_quote, "cron", hour=9, minute=0)  
    scheduler.start()
