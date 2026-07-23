from telegram import Update
from telegram.ext import ContextTypes

from dota_api import get_match
from heroes import get_hero_name
from analyzers.farm_analyzer import analyze_farm


async def analyze_match(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    match_id = update.message.text.strip()


    if not match_id.isdigit():

        await update.message.reply_text(
            "❌ Отправь только ID матча Dota 2.\n\n"
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
            "❌ Матч не найден.\n"
            "Проверь Match ID."
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
            "❌ Данные игроков отсутствуют."
        )

        return



    # Пока анализируем первого игрока
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


    hero_name = get_hero_name(
        hero_id
    )


    gpm = player.get(
        "gold_per_min",
        0
    )


    xpm = player.get(
        "xp_per_min",
        0
    )


    # Анализ фарма
    farm_result = analyze_farm(
        player
    )



    report = (

        "🎮 DOTAMIND AI\n\n"

        f"🆔 Match ID:\n"
        f"{match_id}\n\n"

        f"🦸 Герой:\n"
        f"{hero_name}\n\n"

        f"⚔️ KDA:\n"
        f"{kills}/{deaths}/{assists}\n\n"

        f"💰 GPM: {gpm}\n"
        f"⭐ XPM: {xpm}\n\n"

        f"📊 Анализ фарма:\n"
        f"Оценка: {farm_result['score']}/10\n\n"
        f"{farm_result['comment']}\n\n"

        f"⏱ Длительность игры:\n"
        f"{duration // 60} минут\n\n"

        "✅ Базовый анализ готов.\n"
        "Следующий этап — анализ ошибок."
    )


    await update.message.reply_text(
        report
    )