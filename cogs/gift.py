import discord
from discord.ext import commands

from modules.postgresql import SELECT, COINS
from bot import COMMAND_PREFIX, CHIPS


class Gift(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def gift(self, ctx, member: discord.Member = None, coins: int = 0):
        if not member or coins <= 0:
            return await ctx.channel.send(
                f":x: You must enter the user and the number of Chips {CHIPS} that you want to gift him. For example, `@Kassandra 50`"
            )

        if member.bot:
            return await ctx.channel.send(
                ":x: Robots do not need your money, robots need your love :heart:"
            )

        giver = await self.bot.pg_con.fetchrow(SELECT, ctx.author.id, ctx.guild.id)
        taker = await self.bot.pg_con.fetchrow(SELECT, member.id, member.guild.id)

        if giver["coins"] < coins:
            return await ctx.channel.send(
                f":x: You cannot gift more than what you have on the balance. You can see your balance by entering `{COMMAND_PREFIX}balance`"
            )

        await self.bot.pg_con.execute(
            COINS, ctx.author.id, ctx.guild.id, giver["coins"] - coins,
        )

        await self.bot.pg_con.execute(
            COINS, member.id, member.guild.id, taker["coins"] + coins,
        )

        await ctx.channel.send(
            f"Wow, another gift! {ctx.author.mention} gifted {member.mention} {coins} {CHIPS}"
        )


def setup(bot):
    bot.add_cog(Gift(bot))
