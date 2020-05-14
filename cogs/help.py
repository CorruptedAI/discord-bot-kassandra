import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(color=self.bot.user.color)

        embed.set_author(name='Help', icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        embed.add_field(name='**Flip Coin**', value='`&flip`', inline=True)
        embed.add_field(name='**Roll Dice**', value='`&roll n`', inline=True)
        embed.add_field(name='**Color Game**', value='`&color`', inline=True)
        embed.add_field(name='**Blackjack**', value='`&blackjack`', inline=True)
        embed.add_field(name='**Baccarat**', value='~~`&baccarat`~~', inline=True)
        embed.add_field(name='**Slots**', value='~~`&slots`~~', inline=True)
        embed.add_field(name='**Clear**', value='`&clear n`', inline=True)
        embed.add_field(name='**Ping**', value='`&ping`', inline=True)
        embed.add_field(name='**About**', value='`&about`', inline=True)

        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
