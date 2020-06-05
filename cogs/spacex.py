import discord
from discord.ext import commands
from discord import File

'''
    why not?
'''

class SpaceX(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spacex(self, ctx):
        await ctx.channel.send(file=File('assets/spacex.mp4'))

def setup(bot):
    bot.add_cog(SpaceX(bot))
