import discord
from discord.ext import commands


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        embed = discord.Embed(color=member.color)
        embed.set_image(url=member.avatar_url)
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Avatar(bot))
