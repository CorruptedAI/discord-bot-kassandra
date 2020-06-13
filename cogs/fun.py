import random
import asyncio

import discord
from discord.ext import commands

from discord import File


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.DELAY = 0.5

        # 8-ball answers
        self.answers = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes – definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ]

    @commands.command()
    async def spacex(self, ctx):
        await ctx.channel.send(file=File("assets/spacex.mp4"))

    @commands.command(aliases=["roul"])
    async def roulette(self, ctx):
        msg = await ctx.channel.send("The trigger is pulled")
        await msg.edit(content="The trigger is pulled")
        await asyncio.sleep(self.DELAY * 2)
        if random.randint(1, 6) == 1:
            await msg.edit(content="The trigger is pulled, and the revolver fires!")
            await asyncio.sleep(self.DELAY)
            await msg.edit(
                content="The trigger is pulled, and the revolver fires! {0.author.mention} lies dead in chat.".format(
                    ctx
                )
            )
        else:
            await msg.edit(content="The trigger is pulled, and the revolver clicks.")
            await asyncio.sleep(self.DELAY)
            await msg.edit(
                content="The trigger is pulled, and the revolver clicks. {0.author.mention} has lived to survive roulette!".format(
                    ctx
                )
            )

    @commands.command(pass_context=True)
    async def roll(self, ctx, *arg):
        if len(arg) != 1:
            return await ctx.channel.send("Invalid argument :flushed:".format(ctx))
        embed = discord.Embed(
            title=":game_die: " + str(random.randint(1, int(arg[0]))),
            color=ctx.author.color,
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def m8b(self, ctx, *arg):
        await ctx.channel.send(
            "> "
            + " ".join(arg)
            + "\n{0.author.mention} ".format(ctx)
            + random.choice(self.answers)
        )

    @commands.command()
    async def flip(self, ctx):
        embed = discord.Embed(
            title=random.choice(["Heads", "Tails"]), color=ctx.author.color
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
