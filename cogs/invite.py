import discord
from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        await ctx.channel.send('If you want to invite me to your server, use this link\n<https://bit.ly/kassandrabot>')

def setup(bot):
    bot.add_cog(Invite(bot))
