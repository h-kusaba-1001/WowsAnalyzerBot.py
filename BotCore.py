# インストールした discord.py を読み込む
import discord
import random
import urllib.error
import urllib.request
import json
# from pprint import pprint
from discord.ext import commands
import os
import traceback

# IMPORT FROM OTHER .py FILES
import auth
import config

INITIAL_EXTENSIONS = [
    'cogs.PlayerCog'
]

# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class BotCore(commands.Bot):

    # エラーが発生した場合は、エラー内容を表示。
    def __init__(self, command_prefix):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')

# MyBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    bot = BotCore(command_prefix=config.COMMAND_PREFIX)
    bot.run(auth.DISCORD_TOKEN)