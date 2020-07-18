import discord
from discord.ext import commands

import random
import asyncio

from modules.postgresql import SELECT, TICKETS_COINS


class Duel(commands.Cog):
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
    @commands.guild_only()
    @commands.bot_has_permissions(manage_messages=True)
    async def duel(self, ctx):
        return await ctx.channel.send(
            ":x: Duels are currently being reworked and will be available soon"
        )
        user = await self.bot.pg_con.fetchrow(SELECT, ctx.author.id, ctx.guild.id)

        if user["tickets"] <= 0:
            return await ctx.channel.send(
                f"You do not have enough tickets {TICKETS}. You can purchase them in the `{COMMAND_PREFIX}shop`"
            )
        else:
            await self.bot.pg_con.execute(
                TICKETS, ctx.author.id, ctx.guild.id, user["tickets"] - 2,
            )

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
            await ctx.channel.send(f"Positive, {ctx.author.mention}!")
        else:
            await ctx.channel.send(f"Probably not, {ctx.author.mention}.")

    def update_ui(self, title_m):
        embed = discord.Embed(title=title_m, color=self.bot.user.color)
        embed.set_author(name="Colors Game", icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="You must guess\nwhat color it is\nfaster than anyone")
        return embed


def setup(bot):
    bot.add_cog(Duel(bot))
