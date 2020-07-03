from discord.ext import commands

# コグとして用いるクラスを定義。
class PlayerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # コマンドの作成。コマンドはcommandデコレータで必ず修飾する。
    @commands.command(aliases=['p'])
    async def player(self, ctx):
        await ctx.send('pong!')

def setup(bot):
    bot.add_cog(PlayerCog(bot))