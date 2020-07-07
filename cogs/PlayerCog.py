from discord.ext import commands
import requests
from pprint import pprint
from math import ceil
import datetime

# IMPORT FROM OTHER .py FILES
import conf.auth as auth
import conf.config as config
import conf.message as message
import api.Player
import api.Stats

class PlayerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['p'])
    async def player(self, ctx, player_name: str):

        # API側の仕様により、プレイヤー名は24文字以内とする
        if(len(player_name) > config.API_PLAYER_NAME_LENGTH):
            err_msg = message.player_name_length_error.format(length=config.API_PLAYER_NAME_LENGTH)
            await ctx.send(err_msg)
            return;

        # API プレイヤー名を使用し、アカウントIDを含むdictを取得する
        result_player = api.Player.search_by_player_name(player_name)

        if(not result_player):
            # アカウント名が取得できなかった場合(result_playerが空)、メッセージで返す
            await ctx.send(message.player_not_exists)
            return;
        else:
            #TODO: 検索結果に対し、対話形式で戦績検索アカウントを選択したい
            account_id = result_player[0]['account_id']

        # API アカウントIDを用い、戦績を検索する
        result_stats = api.Stats.get_player_stats(account_id)

        if(result_stats['hidden_profile'] is True): # 戦績非公開
            msg = message.stats_hidden_profile.format(**result_stats)
        elif(result_stats['pvp_battles'] is 0): # 戦闘回数0回のプレイヤーはゼロ除算を起こすため、ここで返す
            msg = message.stats_zero_battles.format(**result_stats)
        else:
            # 検索結果をメッセージで返す
            msg = message.stats.format(**result_stats)

        # 検索結果ごとに作成したメッセージを返す
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(PlayerCog(bot))