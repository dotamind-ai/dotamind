def analyze_draft(
    players
):
    """
    Анализ драфта команды
    """


    radiant = []
    dire = []


    for player in players:

        hero_id = player.get(
            "hero_id",
            0
        )


        team = player.get(
            "isRadiant",
            True
        )


        if team:

            radiant.append(
                hero_id
            )

        else:

            dire.append(
                hero_id
            )



    result = {

        "radiant_count": len(
            radiant
        ),

        "dire_count": len(
            dire
        ),

        "comment": ""
    }



    if len(radiant) == 5 and len(dire) == 5:

        result["comment"] = (
            "⚔️ Оба состава полные.\n"
            "Можно проводить анализ матчапов."
        )

    else:

        result["comment"] = (
            "⚠️ Недостаточно данных "
            "для полного анализа драфта."
        )



    return result