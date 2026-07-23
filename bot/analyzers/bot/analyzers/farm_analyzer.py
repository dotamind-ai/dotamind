def analyze_farm(player):
    """
    Анализирует фарм игрока
    """

    gpm = player.get(
        "gold_per_min",
        0
    )

    xpm = player.get(
        "xp_per_min",
        0
    )


    # Оценка фарма
    if gpm >= 700:
        farm_score = 10
        comment = (
            "🔥 Отличный фарм.\n"
            "Ты создаешь сильное экономическое преимущество."
        )

    elif gpm >= 550:
        farm_score = 8
        comment = (
            "👍 Хороший фарм.\n"
            "Темп экономики выше среднего."
        )

    elif gpm >= 400:
        farm_score = 6
        comment = (
            "⚠️ Средний фарм.\n"
            "Можно улучшить сбор крипов и свободное время."
        )

    else:
        farm_score = 4
        comment = (
            "❌ Слабый фарм.\n"
            "Ты теряешь золото и отстаешь по предметам."
        )


    return {

        "score": farm_score,

        "gpm": gpm,

        "xpm": xpm,

        "comment": comment
    }
