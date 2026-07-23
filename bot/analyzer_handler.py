from telegram import Update
from telegram.ext import ContextTypes


async def analyze_match(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    match_id = update.message.text

    await update.message.reply_text(
        f"🎮 Получил матч: {match_id}\n\n"
        "⏳ Начинаю анализ..."
    )