import requests


OPENDOTA_HEROES_URL = "https://api.opendota.com/api/heroes"


HEROES = {}


def load_heroes():
    """
    Загружает всех героев Dota 2
    """

    global HEROES

    try:
        response = requests.get(
            OPENDOTA_HEROES_URL,
            timeout=10
        )

        if response.status_code != 200:
            print("Не удалось загрузить героев")
            return False


        heroes = response.json()


        for hero in heroes:

            HEROES[hero["id"]] = {
                "name": hero["localized_name"],
                "attribute": hero.get(
                    "primary_attr",
                    "unknown"
                ),
                "attack_type": hero.get(
                    "attack_type",
                    "unknown"
                ),
                "roles": hero.get(
                    "roles",
                    []
                )
            }


        print(
            f"Героев загружено: {len(HEROES)}"
        )

        return True


    except Exception as error:

        print(
            "Ошибка загрузки героев:",
            error
        )

        return False



def get_hero(hero_id):
    """
    Получить полную информацию о герое
    """

    if not HEROES:
        load_heroes()


    return HEROES.get(
        hero_id,
        {
            "name": "Unknown Hero",
            "attribute": "unknown",
            "attack_type": "unknown",
            "roles": []
        }
    )



def get_hero_name(hero_id):
    """
    Получить только имя героя
    """

    hero = get_hero(hero_id)

    return hero["name"]
