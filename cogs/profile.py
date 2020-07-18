import discord
from discord.ext import commands

from modules.time import Time
from modules.postgresql import SELECT
from bot import COMMAND_PREFIX


class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.TWELVE_HOURS = 12 * 60 * 60
        self.time = Time()

    @commands.command()
    @commands.guild_only()
    async def profile(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        if member.bot:
            return await ctx.channel.send(":x: Bots do not have profiles :ghost:")

        user = await self.bot.pg_con.fetchrow(SELECT, member.id, ctx.guild.id)

        embed = discord.Embed(color=member.color)
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        embed.set_thumbnail(url=user["background"])
        embed.add_field(name=":level_slider: Level", value=user["level"], inline=False)
        embed.add_field(name=":comet: Experience", value=user["exp"], inline=False)
        embed.add_field(
            name=":receipt: Description", value=user["description"], inline=False
        )

        ### upd
        embed.set_footer(
            text="This is just an alpha version of the profile,\nsoon the profile will look like a complete picture"
        )
        ###

        try:
            await ctx.channel.send(embed=embed)
        except:
            await ctx.channel.send(
                f":x: If your profile is not shown to you, it means that you have set a nonexistent picture as a background, please enter `{COMMAND_PREFIX}help config` command and see how to change your background"
            )


def setup(bot):
    bot.add_cog(Profile(bot))
