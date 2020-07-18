import discord
from discord.ext import commands

import random

from modules.postgresql import SELECT, TICKETS_COINS
from bot import COMMAND_PREFIX, TICKETS


class M8B(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.answers = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes – definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ]

    @commands.command(aliases=["8b"])
    @commands.guild_only()
    async def m8b(self, ctx, *arg):
        user = await self.bot.pg_con.fetchrow(SELECT, ctx.author.id, ctx.guild.id)

        if user["tickets"] <= 0:
            return await ctx.channel.send(
                f":x: You do not have enough tickets {TICKETS}! You can buy them or win, look here `{COMMAND_PREFIX}shop`"
            )
        else:
            await self.bot.pg_con.execute(
                TICKETS_COINS, ctx.author.id, ctx.guild.id, user["tickets"] - 1,
            )

        await ctx.channel.send(
            f"> {' '.join(arg)}\n{ctx.author.mention} {random.choice(self.answers)}"
        )


def setup(bot):
    bot.add_cog(M8B(bot))
