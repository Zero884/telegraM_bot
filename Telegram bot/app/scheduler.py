import os
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.database import get_random_quote

CHAT_ID = os.getenv("CHAT_ID")


scheduler = AsyncIOScheduler()


async def send_daily_quote(bot: Bot, user_id:int):
    """Надсилає цитату раз на день у вказаний чат."""
    quote = get_random_quote()
    bot.send_message(chat_id=user_id, text=quote)


async def add_job_to_sched():
    scheduler.add_job(send_daily_quote, "cron", hour=9, minute=0)
