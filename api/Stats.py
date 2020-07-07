"""
APIを取得し、使用しやすいdict型で結果を返す
アカウントIDを用いて、PVP戦績を取得して返す
"""
import requests
from math import ceil

# IMPORT FROM OTHER .py FILES
import conf.auth as auth
import conf.config as config
import util.util as util

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
        result['stats_updated_at'] = util.timestamp_format(data['stats_updated_at'])

        # 戦績非公開の場合は、勝率等の計算を行わない
        if(data['hidden_profile'] is False):

            pvp_data = data['statistics']['pvp']
            result['pvp_battles'] = pvp_data['battles']

            # pvp戦闘数が0の場合は、勝率等の計算を行わない
            if(result['pvp_battles'] > 0):
                pvp_wins = pvp_data['wins']
                pvp_survived_battles = pvp_data['survived_battles']
                pvp_damage_dealt = pvp_data['damage_dealt']

                result['win_rate'] = util.calc_rate(pvp_wins, result['pvp_battles'])
                result['survived_rate'] = util.calc_rate(pvp_survived_battles, result['pvp_battles'])
                result['average_damage'] = ceil(pvp_damage_dealt / result['pvp_battles']) # 小数点以下切り上げ

        return result


import sys
sys.modules[__name__]= Stats()