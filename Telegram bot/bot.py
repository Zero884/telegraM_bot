import logging
import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types.bot_command import BotCommand
from app.handlers import router
from app.scheduler import scheduler


load_dotenv()

#TOKEN = os.getenv("TOKEN")

TOKEN = "7712944487:AAFD1SOqaF5Gg5xIWsnEnrblF7JlVEwVDdU"


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)



async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    

    scheduler.start()

    print("Бот запущено!")



    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Зaпуск ботa"),
           
        ]
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
