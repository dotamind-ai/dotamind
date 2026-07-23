def analyze_kda(player):
    """
    Анализ влияния игрока через KDA
    """

    kills = player.get(
        "kills",
        0
    )

    deaths = player.get(
        "deaths",
        0
    )

    assists = player.get(
        "assists",
        0
    )


    kda = (
        kills + assists
    ) / max(
        deaths,
        1
    )


    if kda >= 6:

        score = 10

        comment = (
            "🔥 Огромное влияние на игру.\n"
            "Ты постоянно участвовал в важных моментах."
        )


    elif kda >= 4:

        score = 8

        comment = (
            "👍 Хорошее участие в драках.\n"
            "Ты помогал команде создавать преимущество."
        )


    elif kda >= 2:

        score = 6

        comment = (
            "⚠️ Среднее влияние.\n"
            "Можно чаще участвовать в ключевых событиях."
        )


    else:

        score = 4

        comment = (
            "❌ Низкое влияние на игру.\n"
            "Нужно улучшить участие в командных действиях."
        )


    return {

        "kills": kills,

        "deaths": deaths,

        "assists": assists,

        "kda": round(kda, 2),

        "score": score,

        "comment": comment
    }