import discord
from discord.ext import commands


class Mafia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def mafia(self, ctx):
        await ctx.channel.send("[mafia] coming soon")


def setup(bot):
    bot.add_cog(Mafia(bot))
