from telegram import Update
from telegram.ext import ContextTypes

from dota_api import get_match
from heroes import get_hero_name

from keyboards import players_keyboard
from player_selector import save_players, get_player

from analyzers.match_analyzer import analyze_match as run_player_analysis
from analyzers.draft_analyzer import analyze_draft



async def analyze_match_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.message.from_user.id

    text = update.message.text.strip()



    # Если пользователь отправил номер игрока

    if text.isdigit() and len(text) <= 2:

        player = get_player(
            user_id,
            int(text)
        )


        if not player:

            await update.message.reply_text(
                "❌ Игрок не найден."
            )

            return



        hero_id = player.get(
            "hero_id",
            0
        )


        hero_name = get_hero_name(
            hero_id
        )



        result = run_player_analysis(
            player,
            hero_name
        )



        await update.message.reply_text(

            "🎮 DOTAMIND AI\n\n"

            f"🦸 Герой: {hero_name}\n\n"

            f"{result['summary']}"

        )


        return




    # Если это Match ID


    match_id = text



    await update.message.reply_text(
        "🔎 Ищу матч..."
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




    # сохраняем игроков

    save_players(
        user_id,
        players
    )



    # анализируем драфт

    draft = analyze_draft(
        players
    )



    message = (

        "🎮 Матч найден!\n\n"

        "Выбери игрока для анализа 👇\n\n"

        "⚔️ Анализ драфта:\n"

        f"Оценка состава: {draft['score']}/10\n"

        f"{draft['comment']}"

    )



    await update.message.reply_text(

        message,

        reply_markup=players_keyboard(
            players
        )

    )



analyze_match = analyze_match_command