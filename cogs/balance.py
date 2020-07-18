import discord
from discord.ext import commands

from modules.postgresql import SELECT
from bot import CHIPS, TICKETS


class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bal"])
    @commands.guild_only()
    async def balance(self, ctx):
        user = await self.bot.pg_con.fetchrow(SELECT, ctx.author.id, ctx.guild.id)
        embed = discord.Embed(color=ctx.author.color)
        embed.set_author(name="Balance", icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"{CHIPS} Chips", value=user["coins"], inline=True)
        embed.add_field(name=f"{TICKETS} Tickets", value=user["tickets"], inline=True)

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Balance(bot))
