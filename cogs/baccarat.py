import discord
from discord.ext import commands


class Baccarat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["baccara", "bac"])
    @commands.guild_only()
    @commands.bot_has_permissions(manage_emojis=True, manage_messages=True)
    async def baccarat(self, ctx):
        await ctx.channel.send("[baccarat] coming soon")


def setup(bot):
    bot.add_cog(Baccarat(bot))
