from heroes import get_hero_name


def convert_hero_id(hero_id):
    """
    Перевод ID героя в название
    """

    hero_name = get_hero_name(
        hero_id
    )


    if not hero_name:

        return "Unknown"


    return hero_name