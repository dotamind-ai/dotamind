def analyze_items(player):
    """
    Анализ предметов игрока
    """

    items = []


    for i in range(6):

        item_id = player.get(
            f"item_{i}",
            0
        )

        if item_id != 0:

            items.append(
                item_id
            )



    item_count = len(
        items
    )


    if item_count >= 6:

        score = 10

        comment = (
            "🔥 Полный набор предметов.\n"
            "Игрок хорошо использовал золото."
        )


    elif item_count >= 4:

        score = 7

        comment = (
            "👍 Нормальный билд.\n"
            "Есть место для улучшения."
        )


    else:

        score = 5

        comment = (
            "⚠️ Мало информации о предметах.\n"
            "Нужно больше данных."
        )



    return {

        "items": items,

        "count": item_count,

        "score": score,

        "comment": comment
    }