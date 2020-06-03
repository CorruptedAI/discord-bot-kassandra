import random
import asyncio

import discord
from discord.ext import commands

class Russian_Roulette(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.DELAY = .5

    @commands.command(aliases=['roul'])
    async def roulette(self, ctx):
        msg = await ctx.channel.send('The trigger is pulled')
        await msg.edit(content='The trigger is pulled')
        await asyncio.sleep(self.DELAY*2)
        if random.randint(1, 6) == 1:
            await msg.edit(content='The trigger is pulled, and the revolver fires!')
            await asyncio.sleep(self.DELAY)
            await msg.edit(content='The trigger is pulled, and the revolver fires! {0.author.mention} lies dead in chat.'.format(ctx))
        else:
            await msg.edit(content='The trigger is pulled, and the revolver clicks.')
            await asyncio.sleep(self.DELAY)
            await msg.edit(content='The trigger is pulled, and the revolver clicks. {0.author.mention} has lived to survive roulette!'.format(ctx))


def setup(bot):
    bot.add_cog(Russian_Roulette(bot))
