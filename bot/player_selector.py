players_cache = {}


def save_players(
    user_id,
    players
):

    players_cache[user_id] = players



def get_players(
    user_id
):

    return players_cache.get(
        user_id,
        []
    )



def get_player(
    user_id,
    number
):

    players = get_players(
        user_id
    )


    index = number - 1


    if index < 0 or index >= len(players):

        return None


    return players[index]