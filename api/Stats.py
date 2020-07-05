"""
APIを取得し、使用しやすいdict型で結果を返す
アカウントIDを用いて、PVP戦績を取得して返す
"""
import requests

# IMPORT FROM OTHER .py FILES
import auth
import config
from pprint import pprint
from math import ceil
import datetime

class Stats(object):

    @staticmethod
    def get_player_stats(account_id: str):

        result = {}

        personal_data_get_parameters = {
            'application_id': auth.WARGAMING_APP_TOKEN,
            'account_id': account_id
        }

        res = requests.get(config.PERSONAL_DATA_WOWS_API_URL, params=personal_data_get_parameters)

        jsonData = res.json()

        # APIの結果
        data = jsonData['data'][str(account_id)]

        # APIの結果とは別に、dict型のresultを作成し、そのままメッセージに使用できるようにする
        result['nickname'] = data['nickname']
        result['hidden_profile'] = data['hidden_profile']
        result['stats_updated_at'] = datetime.datetime.fromtimestamp(data['stats_updated_at'], datetime.timezone(datetime.timedelta(hours=config.TIMEZONE_HOURS)))


        # 戦績非公開の場合は、勝率等の計算を行わない
        if(data['hidden_profile'] is False):

            pvp_data = data['statistics']['pvp']
            result['pvp_battles'] = pvp_data['battles']

            # pvp戦闘数が0の場合は、勝率等の計算を行わない
            if(result['pvp_battles'] > 0):
                pvp_wins = pvp_data['wins']
                pvp_survived_battles = pvp_data['survived_battles']
                pvp_damage_dealt = pvp_data['damage_dealt']

                result['win_rate'] = round(pvp_wins * 100 / result['pvp_battles'], 2)
                result['survived_rate'] = round(pvp_survived_battles * 100 / result['pvp_battles'], 2)
                result['damage_rate'] = ceil(pvp_damage_dealt / result['pvp_battles'])

        return result


import sys
sys.modules[__name__]= Stats()