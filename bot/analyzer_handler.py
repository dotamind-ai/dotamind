from telegram import Update
from telegram.ext import ContextTypes

from dota_api import get_match


async def analyze_match(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    match_id = update.message.text.strip()

    await update.message.reply_text(
        "🔎 Ищу матч Dota 2..."
    )

    match = get_match(match_id)

    if not match:
        await update.message.reply_text(
            "❌ Матч не найден.\n"
            "Проверь правильность ID."
        )
        return

    duration = match.get("duration", 0)
    players = match.get("players", [])

    await update.message.reply_text(
        "🎮 Dotamind анализ\n\n"
        f"⏱ Длительность: {duration // 60} минут\n"
        f"👥 Игроков найдено: {len(players)}\n\n"
        "✅ Данные матча получены."
    )