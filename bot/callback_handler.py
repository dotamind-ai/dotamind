from telegram import Update
from telegram.ext import ContextTypes

from player_selector import get_player

from heroes import get_hero_name

from analyzers.match_analyzer import analyze_match



async def player_selected(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query


    await query.answer()



    user_id = query.from_user.id



    number = int(
        query.data.split("_")[1]
    )



    player = get_player(
        user_id,
        number
    )


    if not player:

        await query.message.reply_text(
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



    result = analyze_match(
        player,
        hero_name
    )



    await query.message.reply_text(

        "🎮 DOTAMIND AI\n\n"

        f"🦸 {hero_name}\n\n"

        f"{result['summary']}"

    )