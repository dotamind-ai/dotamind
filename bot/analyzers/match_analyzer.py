from analyzers.farm_analyzer import analyze_farm
from analyzers.death_analyzer import analyze_deaths
from analyzers.kda_analyzer import analyze_kda



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


    kda = analyze_kda(
        player
    )


    summary = generate_summary(
        hero_name,
        farm,
        deaths,
        kda
    )


    return {

        "hero": hero_name,

        "farm": farm,

        "deaths": deaths,

        "kda": kda,

        "summary": summary
    }




def generate_summary(
        hero_name,
        farm,
        deaths,
        kda
):

    messages = []


    messages.append(
        f"🧠 Анализ игры на {hero_name}"
    )


    messages.append(
        f"⚔️ KDA: {kda['kda']}\n"
        f"{kda['comment']}"
    )


    messages.append(
        f"💰 Фарм: {farm['score']}/10\n"
        f"{farm['comment']}"
    )


    messages.append(
        f"☠️ Смерти: {deaths['deaths']}\n"
        f"{deaths['comment']}"
    )


    messages.append(
        "📈 Следующий этап — анализ "
        "предметов, талантов и решений игрока."
    )


    return "\n\n".join(
        messages
    )