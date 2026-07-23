from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from heroes import get_hero_name



def players_keyboard(players):

    buttons = []


    for index, player in enumerate(players, start=1):

        hero_id = player.get(
            "hero_id",
            0
        )


        hero_name = get_hero_name(
            hero_id
        )


        buttons.append(

            [
                InlineKeyboardButton(
                    text=f"{index}. {hero_name}",
                    callback_data=f"player_{index}"
                )
            ]

        )


    return InlineKeyboardMarkup(
        buttons
    )