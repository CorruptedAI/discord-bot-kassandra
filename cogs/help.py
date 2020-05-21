import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx, arg='default'):
        embed = discord.Embed(title='Command prefix: `&`',
                              color=self.bot.user.color)

        embed.set_author(name='Help', icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        if arg == 'default':
            embed.add_field(name='**Games**', value='`help games`', inline=True)
            embed.add_field(name='**Stats**', value='~~`stats @n`~~', inline=True)
            embed.add_field(name='**Balance**', value='~~`balance`~~', inline=True)
            embed.add_field(name='**Daily Bonus**', value='~~`daily`~~', inline=True)
            embed.add_field(name='**Utilities**', value='`help util`', inline=True)
            embed.add_field(name='**About**', value='`about`', inline=True)

        elif arg == 'games':
            embed.add_field(name='**Coinflip**\t\t\t\t\t', value='`flip`', inline=False)
            embed.add_field(name='**Roll Dice**', value='`roll n`', inline=False)
            embed.add_field(name='**Color Game**', value='`color`', inline=False)
            embed.add_field(name='**Russian Roulette\t**', value='~~`roulette`~~', inline=False)
            embed.add_field(name='**Blackjack**', value='`blackjack`', inline=False)
            embed.add_field(name='**Baccarat**', value='~~`baccarat`~~', inline=False)
            embed.add_field(name='**Slots**', value='`slots`', inline=False)

        elif arg == 'util':
            embed.add_field(name='**Change Prefix**', value='~~`prefix`~~', inline=False)
            embed.add_field(name='**Clear**', value='`clear n`', inline=False)
            embed.add_field(name='**Ping**', value='`ping`', inline=False)

        else:
            embed.add_field(name='**Invalid argument** :flushed:', value='Try **`&help`**', inline=False)

        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
