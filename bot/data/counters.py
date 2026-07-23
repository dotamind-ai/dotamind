# Dotamind AI
# База контрпиков героев Dota 2


COUNTERS = {


}


def get_counters(hero_name):

    hero = COUNTERS.get(
        hero_name
    )

    if not hero:

        return {
            "counters": [],
            "strong_against": []
        }


    return hero