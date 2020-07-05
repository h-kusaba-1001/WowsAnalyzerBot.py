from discord.ext import commands
import requests
from pprint import pprint
from math import ceil
import datetime

# IMPORT FROM OTHER .py FILES
import auth
import config
import conf.message as message

# コグとして用いるクラスを定義。
class PlayerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # コマンドの作成。コマンドはcommandデコレータで必ず修飾する。
    @commands.command(aliases=['p'])
    async def player(self, ctx, player_name: str):

        players_get_parameters = {
            'application_id': auth.WARGAMING_APP_TOKEN,
            'search': player_name,
            'limit': 1
        }

        res = requests.get(config.PLAYERS_WOWS_API_URL, params=players_get_parameters)

        jsonData = res.json()

        if(not jsonData['data']):
            # アカウント名がないので返す
            await ctx.send(message.player_not_exists)
            return;
        else:
            account_id = jsonData['data'][0]['account_id']

        personal_data_get_parameters = {
            'application_id': auth.WARGAMING_APP_TOKEN,
            'account_id': account_id
        }

        res = requests.get(config.PERSONAL_DATA_WOWS_API_URL, params=personal_data_get_parameters)

        jsonData = res.json()

        data = jsonData['data'][str(account_id)]

        if(data['hidden_profile'] is True):
            await ctx.send(message.players_stats_hidden_profile)
            return;

        stats_updated_at = datetime.datetime.fromtimestamp(data['stats_updated_at'], datetime.timezone(datetime.timedelta(hours=config.TIMEZONE_HOURS)))
        nickname = data['nickname']

        pvp_data = data['statistics']['pvp']

        pvp_battles = pvp_data['battles']
        pvp_wins = pvp_data['wins']
        pvp_survived_battles = pvp_data['survived_battles']
        pvp_damage_dealt = pvp_data['damage_dealt']

        win_rate = round(pvp_wins * 100 / pvp_battles, 2)
        survived_rate = round(pvp_survived_battles * 100 / pvp_battles, 2)
        damage_rate = ceil(pvp_damage_dealt / pvp_battles)

        comment = message.stats.format(
            nickname=nickname,
            pvp_battles=pvp_battles,
            win_rate=win_rate,
            damage_rate=damage_rate,
            survived_rate=survived_rate,
            stats_updated_at=stats_updated_at
        )
        await ctx.send(comment)

def setup(bot):
    bot.add_cog(PlayerCog(bot))