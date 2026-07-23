from telegram import Update
from telegram.ext import ContextTypes


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "🎮 Привет! Я Dotamind AI.\n\n"
        "Отправь мне ID матча Dota 2, "
        "и я сделаю анализ игры."
    )