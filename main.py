# インストールした discord.py を読み込む
import discord
from discord.ext import commands
import traceback
import keyword

# IMPORT FROM OTHER .py FILES
import conf.auth as auth
import conf.config as config

# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class BotCore(commands.Bot):

    # エラーが発生した場合は、エラー内容を表示。
    def __init__(self, command_prefix):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix)

        for cog in config.cogs:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        print('Ready!')

# MyBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    print(config.COMMAND_PREFIX)
    bot = BotCore(command_prefix=config.COMMAND_PREFIX)
    bot.run(auth.DISCORD_TOKEN)