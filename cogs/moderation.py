import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def clear(self, ctx, arg=1):
        await ctx.channel.purge(limit=arg + 1)

    @clear.error
    async def clear_error(self, error, ctx):
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            await ctx.channel.send("You don't have permission to `clear`.")


def setup(bot):
    bot.add_cog(Moderation(bot))
