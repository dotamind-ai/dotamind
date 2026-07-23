from telegram import InlineKeyboardButton, InlineKeyboardMarkup



def players_keyboard(players):

    buttons = []


    for index, player in enumerate(players, start=1):

        hero_name = player.get(
            "hero_name",
            f"Игрок {index}"
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