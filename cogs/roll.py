import random

import discord
from discord.ext import commands

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def roll(self, ctx, *arg):
        if len(arg) != 1:
            return await ctx.channel.send('I can take only one argument, {0.author.mention} D:'.format(ctx))
        embed = discord.Embed(title=':game_die: ' + str(random.randint(1, int(arg[0]))), color=ctx.author.color)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Roll(bot))
