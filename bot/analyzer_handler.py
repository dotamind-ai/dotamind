from telegram import Update
from telegram.ext import ContextTypes

from dota_api import get_match
from heroes import get_hero_name

from analyzers.match_analyzer import analyze_match



async def analyze_match_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    match_id = update.message.text.strip()


    if not match_id.isdigit():

        await update.message.reply_text(
            "❌ Отправь ID матча Dota 2.\n\n"
            "Пример:\n"
            "8123456789"
        )

        return



    await update.message.reply_text(
        "🔎 Анализирую матч..."
    )



    match = get_match(
        match_id
    )


    if not match:

        await update.message.reply_text(
            "❌ Матч не найден."
        )

        return



    players = match.get(
        "players",
        []
    )


    if not players:

        await update.message.reply_text(
            "❌ Игроки не найдены."
        )

        return



    # Пока берем первого игрока
    player = players[0]



    hero_id = player.get(
        "hero_id",
        0
    )


    hero_name = get_hero_name(
        hero_id
    )



    analysis = analyze_match(
        player,
        hero_name
    )



    report = (

        "🎮 DOTAMIND AI\n\n"

        f"🦸 Герой:\n"
        f"{analysis['hero']}\n\n"

        f"{analysis['summary']}"
    )



    await update.message.reply_text(
        report
    )