import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def clear(self, ctx, arg=1):
        await ctx.channel.purge(limit=arg+1)

def setup(bot):
    bot.add_cog(Moderation(bot))
