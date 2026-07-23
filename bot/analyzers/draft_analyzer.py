from data.heroes_meta import get_hero_meta



def analyze_draft(players):

    """
    Анализ состава команд
    """


    heroes = []


    for player in players:

        hero_id = player.get(
            "hero_id",
            0
        )


        heroes.append(
            hero_id
        )



    result = {

        "heroes_count": len(
            heroes
        ),

        "comment": ""

    }



    if len(heroes) == 10:

        result["comment"] = (
            "⚔️ Полный драфт найден.\n"
            "Можно анализировать матчапы."
        )


    else:

        result["comment"] = (
            "⚠️ Данных недостаточно "
            "для полного анализа драфта."
        )


    return result