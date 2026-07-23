def analyze_farm(player):

    gpm = player.get(
        "gold_per_min",
        0
    )

    xpm = player.get(
        "xp_per_min",
        0
    )


    if gpm >= 700:

        score = 10

        comment = (
            "🔥 Отличный фарм.\n"
            "Ты очень эффективно используешь время."
        )


    elif gpm >= 550:

        score = 8

        comment = (
            "👍 Хороший фарм.\n"
            "Экономика развивается нормально."
        )


    elif gpm >= 400:

        score = 6

        comment = (
            "⚠️ Средний фарм.\n"
            "Можно лучше контролировать крипов."
        )


    else:

        score = 4

        comment = (
            "❌ Слабый фарм.\n"
            "Ты теряешь золото и отстаешь по предметам."
        )


    return {
        "score": score,
        "gpm": gpm,
        "xpm": xpm,
        "comment": comment
    }