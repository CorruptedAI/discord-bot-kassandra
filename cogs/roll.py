import discord
from discord.ext import commands

import random

from modules.postgresql import SELECT, TICKETS_COINS
from bot import COMMAND_PREFIX, TICKETS


class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def roll(self, ctx, num: int = 6):
        user = await self.bot.pg_con.fetchrow(SELECT, ctx.author.id, ctx.guild.id)

        if user["tickets"] <= 0:
            return await ctx.channel.send(
                f":x: You do not have enough tickets {TICKETS}! You can buy them or win, look here `{COMMAND_PREFIX}shop`"
            )
        else:
            await self.bot.pg_con.execute(
                TICKETS_COINS, ctx.author.id, ctx.guild.id, user["tickets"] - 1,
            )

        embed = discord.Embed(
            title=f":game_die: {random.randint(1, num)}", color=ctx.author.color,
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Roll(bot))
