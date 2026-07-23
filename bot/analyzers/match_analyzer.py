from analyzers.farm_analyzer import analyze_farm
from analyzers.death_analyzer import analyze_deaths


def analyze_match(player, hero_name):
    """
    Главный анализатор матча
    """


    farm = analyze_farm(
        player
    )


    deaths = analyze_deaths(
        player
    )


    report = {

        "hero": hero_name,


        "farm": farm,


        "deaths": deaths,


        "summary": generate_summary(
            hero_name,
            farm,
            deaths
        )
    }


    return report



def generate_summary(
        hero_name,
        farm,
        deaths
):

    messages = []


    messages.append(
        f"🧠 Анализ игры на {hero_name}"
    )


    if farm["score"] <= 5:

        messages.append(
            "💰 Проблема: слабый фарм.\n"
            "Работай над добиванием крипов "
            "и временем между действиями."
        )

    else:

        messages.append(
            "💰 Фарм выглядит хорошо."
        )



    if deaths["score"] <= 5:

        messages.append(
            "☠️ Много смертей.\n"
            "Следи за позицией перед драками."
        )

    else:

        messages.append(
            "🛡 Хорошая выживаемость."
        )


    messages.append(
        "📈 Анализ будет становиться точнее "
        "с добавлением новых модулей."
    )


    return "\n\n".join(
        messages
    )