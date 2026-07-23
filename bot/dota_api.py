import requests


OPENDOTA_URL = "https://api.opendota.com/api/matches/"


def get_match(match_id):

    url = OPENDOTA_URL + str(match_id)

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return None

        match_data = response.json()

        return match_data

    except Exception as error:
        print("Ошибка получения матча:", error)
        return None
