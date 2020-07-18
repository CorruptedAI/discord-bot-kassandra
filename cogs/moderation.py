from discord.ext import commands
from discord.ext.commands import has_permissions

import discord
import asyncio


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 1):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount} messages have been just deleted")
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(":x: You don't have enough permission to do that")
        if isinstance(error, commands.BadArgument):
            await ctx.send(":x: Invalid argument")
        raise error


def setup(bot):
    bot.add_cog(Moderation(bot))
