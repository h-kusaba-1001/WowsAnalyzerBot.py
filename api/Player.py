"""
APIを取得し、使用しやすいdict型で結果を返す
プレイヤーを返す
"""
import requests

# IMPORT FROM OTHER .py FILES
import auth
import config
from pprint import pprint

class Player(object):

    @staticmethod
    def search_by_player_name(player_name: str):

        result = {}

        players_get_parameters = {
            'application_id': auth.WARGAMING_APP_TOKEN,
            'search': player_name,
            'limit': 1
        }

        res = requests.get(config.PLAYERS_WOWS_API_URL, params=players_get_parameters)

        jsonData = res.json()

        if(not jsonData['data']):
            pass
        else:
            # Playerが見つかった場合、dataの中身を返す
            result = jsonData['data']

        return result


import sys
sys.modules[__name__]= Player()