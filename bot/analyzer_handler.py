from telegram import Update
from telegram.ext import ContextTypes

from dota_api import get_match
from heroes import get_hero_name

from analyzers.match_analyzer import analyze_match as run_player_analysis
from analyzers.draft_analyzer import analyze_draft



async def analyze_match_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    match_id = update.message.text.strip()


    if not match_id.isdigit():

        await update.message.reply_text(
            "❌ Отправь ID матча Dota 2."
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



    # Анализ всего драфта
    draft = analyze_draft(
        players
    )



    # Пока берем первого игрока
    player = players[0]


    hero_id = player.get(
        "hero_id",
        0
    )


    hero_name = get_hero_name(
        hero_id
    )



    player_analysis = run_player_analysis(
        player,
        hero_name
    )



    report = (

        "🎮 DOTAMIND AI\n\n"

        f"🦸 Герой: {hero_name}\n\n"

        f"⚔️ Анализ драфта:\n"
        f"Оценка: {draft['score']}/10\n"
        f"{draft['comment']}\n\n"

        f"{player_analysis['summary']}"
    )



    await update.message.reply_text(
        report
    )



analyze_match = analyze_match_command