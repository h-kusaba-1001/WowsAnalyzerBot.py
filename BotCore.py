# インストールした discord.py を読み込む
import discord
import random
import urllib.error
import urllib.request
import json
import yaml
# from pprint import pprint
from discord.ext import commands
import os
import traceback

INITIAL_EXTENSIONS = [
    'cogs.PlayerCog'
]

# gitignoreのauth.jsonの有無で、テスト環境・本番環境を分ける。(herokuでgitを使うため)
if(os.path.exists("auth.yaml")):
    # 検証環境等では、auth.yamlからログイン情報を読み取る
    with open('auth.yaml', 'r') as auth_yaml:
        auth = yaml.load(auth_yaml, Loader=yaml.SafeLoader)
        DISCORD_TOKEN = auth["DISCORD_TOKEN"]
        WARGAMING_APP_TOKEN = auth["WARGAMING_APP_TOKEN"]
        auth_yaml.close()
else:
    # 本番環境では、herokuの環境変数を読み取る。
    DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
    WARGAMING_APP_TOKEN = os.environ["WARGAMING_APP_TOKEN"]

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
    bot = BotCore(command_prefix='-') # command_prefixはコマンドの最初の文字として使うもの。 e.g. !ping
    bot.run(DISCORD_TOKEN) # Botのトークン