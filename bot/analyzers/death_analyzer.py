def analyze_deaths(player):
    """
    Анализ смертей игрока
    """

    deaths = player.get(
        "deaths",
        0
    )


    if deaths <= 3:

        score = 10

        comment = (
            "🔥 Отличная выживаемость.\n"
            "Ты хорошо выбирал позиции "
            "и не отдавал лишние смерти."
        )


    elif deaths <= 7:

        score = 7

        comment = (
            "👍 Нормальное количество смертей.\n"
            "Есть моменты, где можно было играть осторожнее."
        )


    else:

        score = 4

        comment = (
            "❌ Слишком много смертей.\n"
            "Ты часто отдавал преимущество врагу."
        )


    return {

        "score": score,

        "deaths": deaths,

        "comment": comment
    }