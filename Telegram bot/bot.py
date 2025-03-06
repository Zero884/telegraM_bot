import logging
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from apscheduler.schedulers.background import BackgroundScheduler
from app.handlers import setup_handlers
from app.quotes import get_random_quote

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def send_daily_quote(app):
    """Надсилає цитату раз на день у вказаний чат."""
    quote = get_random_quote()
    app.bot.send_message(chat_id=CHAT_ID, text=quote)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    setup_handlers(app)

    scheduler = BackgroundScheduler()
    scheduler.add_job(send_daily_quote, "interval", hours=24, args=[app])  
    scheduler.start()

    print("Бот запущено!")
    app.run_polling()

if __name__ == "__main__":
    main()
