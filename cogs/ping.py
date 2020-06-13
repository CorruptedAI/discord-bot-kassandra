import random

import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="{0:.0f}".format(self.bot.latency * 1000) + "ms",
            color=self.bot.user.color,
        )
        embed.set_author(name="Pong!", icon_url=self.bot.user.avatar_url)
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Ping(bot))
