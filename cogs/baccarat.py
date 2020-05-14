import random

import discord
from discord.ext import commands

class Baccarat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def baccarat(self, ctx):
        await ctx.channel.send('coming soon...')

def setup(bot):
    bot.add_cog(Baccarat(bot))
