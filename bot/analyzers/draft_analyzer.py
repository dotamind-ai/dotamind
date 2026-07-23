from data.roles import get_roles
from data.hero_converter import convert_hero_id



def analyze_draft(players):

    """
    Анализ состава команд
    """


    roles = []

    heroes = []



    for player in players:

        hero_id = player.get(
            "hero_id",
            0
        )


        hero_name = convert_hero_id(
            hero_id
        )


        heroes.append(
            hero_name
        )


        hero_roles = get_roles(
            hero_name
        )


        roles.extend(
            hero_roles
        )



    carry_count = roles.count(
        "Carry"
    )

    support_count = roles.count(
        "Support"
    )

    initiator_count = roles.count(
        "Initiator"
    )



    score = 10

    problems = []



    if carry_count >= 3:

        score -= 2

        problems.append(
            "⚠️ Слишком много героев требуют фарма."
        )



    if support_count == 0:

        score -= 2

        problems.append(
            "⚠️ Нет поддержки."
        )



    if initiator_count == 0:

        score -= 2

        problems.append(
            "⚠️ Нет героя для начала драки."
        )



    if score < 0:

        score = 0



    if not problems:

        comment = (
            "✅ Состав выглядит сбалансированным."
        )

    else:

        comment = "\n".join(
            problems
        )



    return {

        "score": score,

        "heroes": heroes,

        "carry": carry_count,

        "support": support_count,

        "initiator": initiator_count,

        "comment": comment
    }