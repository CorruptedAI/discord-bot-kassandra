import random
import asyncio

import discord
from discord.ext import commands


class Color(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.delay = 0.5

        self.colors_list = {
            "red": ":heart:",
            "orange": ":orange_heart:",
            "yellow": ":yellow_heart:",
            "green": ":green_heart:",
            "blue": ":blue_heart:",
            "purple": ":purple_heart:",
            "black": ":black_heart:",
            "brown": ":brown_heart:",
            "white": ":white_heart:",
        }
        self.colors = []
        for c in self.colors_list:
            self.colors.append(c)

    @commands.command()
    async def colors(self, ctx):
        embed = self.update_ui("3..")
        msg = await ctx.channel.send(embed=embed)
        await msg.edit(embed=embed)
        await asyncio.sleep(self.delay)

        embed = self.update_ui("2..")
        await msg.edit(embed=embed)
        await asyncio.sleep(self.delay)

        embed = self.update_ui("1..")
        await msg.edit(embed=embed)
        await asyncio.sleep(self.delay)

        color = random.choice(self.colors)

        embed = self.update_ui(self.colors_list.get(color))
        await msg.edit(embed=embed)

        try:
            checkin = await self.bot.wait_for("message", check=None, timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.channel.send("You took too long. Your frame was closed.")

        if checkin.content.lower() == color:
            await ctx.channel.send("Positive, {0.author.mention}!".format(ctx))
        else:
            await ctx.channel.send("Probably not, {0.author.mention}.".format(ctx))

    def update_ui(self, title_m):
        embed = discord.Embed(title=title_m, color=self.bot.user.color)
        embed.set_author(name="Colors Game", icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="You must guess\nwhat color it is\nfaster than anyone")
        return embed


def setup(bot):
    bot.add_cog(Color(bot))
