import random

import discord
from discord.ext import commands

class Flip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        embed = discord.Embed(title=random.choice(['Heads', 'Tails']), color=ctx.author.color)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Flip(bot))
