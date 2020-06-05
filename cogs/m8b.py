import random

import discord
from discord.ext import commands

class M8B(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.answers = ['It is certain.',
                        'It is decidedly so.',
                        'Without a doubt.',
                        'Yes – definitely.',
                        'You may rely on it.',
                        'As I see it, yes.',
                        'Most likely.',
                        'Outlook good.',
                        'Yes.',
                        'Signs point to yes.',

                        'Reply hazy, try again.',
                        'Ask again later.',
                        'Better not tell you now.',
                        'Cannot predict now.',
                        'Concentrate and ask again.',

                        'Don\'t count on it.',
                        'My reply is no.',
                        'My sources say no.',
                        'Outlook not so good.',
                        'Very doubtful.'
        ]

    @commands.command(pass_context=True)
    async def m8b(self, ctx, *arg):
        await ctx.channel.send('> ' + ' '.join(arg) + '\n{0.author.mention} '.format(ctx) + random.choice(self.answers))

def setup(bot):
    bot.add_cog(M8B(bot))
