import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
import random
from datetime import datetime
import requests
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
TOKEN = "7717642596:AAGh-U7r5qfy8GKY5QXYwjXi4Erk9IP9B1Y"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! 👋\n\n"
        f"Я CuteVanyaaaBot:\n"
        f"1. /start - показать это сообщение\n"
        f"2. /help - получить справку\n"
        f"3. /random - случайное число от 1 до 100\n"
        f"4. /weather [город] - узнать погоду\n"
        f"5. /time - показать текущее время\n\n"
        f"Чем могу помочь?"
    )
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Случайное число", callback_data="random"),
            InlineKeyboardButton("Текущее время", callback_data="time"),
        ],
        [InlineKeyboardButton("Погода", callback_data="weather")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Выберите функцию, которую хотите использовать:",
        reply_markup=reply_markup
    )
