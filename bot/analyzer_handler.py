from telegram import Update
from telegram.ext import ContextTypes

from dota_api import get_match


async def analyze_match(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    match_id = update.message.text.strip()

    # Проверяем, что пользователь отправил число
    if not match_id.isdigit():
        await update.message.reply_text(
            "❌ Отправь только Match ID Dota 2.\n\n"
            "Пример:\n"
            "8123456789"
        )
        return


    await update.message.reply_text(
        "🔎 Ищу матч Dota 2..."
    )


    match = get_match(match_id)


    if not match:
        await update.message.reply_text(
            "❌ Не удалось найти матч.\n"
            "Проверь ID и попробуй снова."
        )
        return


    duration = match.get(
        "duration",
        0
    )


    players = match.get(
        "players",
        []
    )


    if len(players) == 0:
        await update.message.reply_text(
            "❌ В матче нет данных игроков."
        )
        return


    # Берем первого игрока
    player = players[0]


    kills = player.get(
        "kills",
        0
    )

    deaths = player.get(
        "deaths",
        0
    )

    assists = player.get(
        "assists",
        0
    )

    hero_id = player.get(
        "hero_id",
        0
    )

    gpm = player.get(
        "gold_per_min",
        0
    )

    xpm = player.get(
        "xp_per_min",
        0
    )


    report = (
        "🎮 Dotamind AI\n\n"
        f"🆔 Match ID: {match_id}\n\n"
        f"⏱ Длительность: "
        f"{duration // 60} минут\n\n"
        f"⚔️ KDA:\n"
        f"{kills}/{deaths}/{assists}\n\n"
        f"💰 GPM: {gpm}\n"
        f"⭐ XPM: {xpm}\n\n"
        f"🦸 Hero ID: {hero_id}\n\n"
        "✅ Данные матча получены.\n"
        "Следующий этап: анализ ошибок игрока."
    )


    await update.message.reply_text(
        report
    )