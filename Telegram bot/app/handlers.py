from telegram.ext import CommandHandler
from app.commands import start_command, help_command, quote_command

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("quote", quote_command))