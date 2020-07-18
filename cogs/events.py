import discord
from discord.ext import commands

from modules.time import Time
from modules.postgresql import SELECT, DEFAULT_VALUES
from bot import COMMAND_PREFIX


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member == self.bot.user or member.bot:
            return

        user = await self.bot.pg_con.fetchrow(SELECT, member.id, member.guild.id)

        if not user:
            await self.bot.pg_con.fetchrow(DEFAULT_VALUES, member.id, member.guild.id)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for member in guild.members:
            if not (member == self.bot.user or member.bot):
                user = await self.bot.pg_con.fetchrow(SELECT, member.id, guild.id)

                if not user:
                    await self.bot.pg_con.fetchrow(DEFAULT_VALUES, member.id, guild.id)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.channel.send(
                f":x: You cannot use this command in DM. Enter `{COMMAND_PREFIX}help` to see more information about it"
            )
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.channel.send(
                ":x: I do not have permission on this server to use this command. Please contact the server administrator to fix this problem"
            )
        else:
            raise error


def setup(bot):
    bot.add_cog(Events(bot))
