import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['h'])
    async def help(self, ctx, arg='default'):
        embed = discord.Embed(title='Command prefix: `&`',
                              description='Use &help [command] for get more information',
                              color=self.bot.user.color)

        embed.set_author(name='Help', icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        if arg == 'default':
            embed.add_field(name='**Games**',
                            #value='`blackjack` `baccarat` `slots` `mafia`', 
                            value='`blackjack` `slots`', 
                            inline=True)

            embed.add_field(name='**Fun**',
                            value='`flip` `roll` `roulette` `colors` `m8b` `spacex`', 
                            inline=True)

            embed.add_field(name='**Economy**',
                            #value='`balance` `daily` `shop` `stats`',
                            value='soon',
                            inline=True)

            embed.add_field(name='**Information**',
                            #value='`info` `avatar` `server` `channel` `about`',
                            value='`about`',
                            inline=True)

            embed.add_field(name='**Utilities**',
                            #value='`weather` `remind` `invite` `ping`',
                            value='`weather` `invite` `ping`',
                            inline=True)

            embed.add_field(name='**Moderation**\n[for admins only]',
                            #value='`clear` `kick` `ban` `unban`',
                            value='`clear`',
                            inline=True)
        else:
            embed.add_field(name='**Invalid argument** :flushed:', value='Try **`&help`**', inline=False)

        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
