import discord
from discord.ext import commands
from discord.utils import get

import asyncio
import random

from modules.postgresql import SELECT, TICKETS_COINS
from bot import COMMAND_PREFIX, TICKETS


class Roulette(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.DELAY = 0.5
        self.reincarnation = 10 * 60

    @commands.command(aliases=["roul"])
    @commands.guild_only()
    @commands.bot_has_permissions(manage_messages=True, manage_roles=True)
    async def roulette(self, ctx):
        user = await self.bot.pg_con.fetchrow(SELECT, ctx.author.id, ctx.guild.id)

        if user["tickets"] <= 0:
            return await ctx.channel.send(
                f":x: You do not have enough tickets {TICKETS}! You can buy them or win, look here `{COMMAND_PREFIX}shop`"
            )
        else:
            await self.bot.pg_con.execute(
                TICKETS_COINS, ctx.author.id, ctx.guild.id, user["tickets"] - 1,
            )

        msg = await ctx.channel.send("The trigger is pulled")
        await msg.edit(content="The trigger is pulled")
        await asyncio.sleep(self.DELAY * 2)

        if random.randint(1, 2) == 1:
            # if random.randint(1, 6) == 1:
            await msg.edit(content="The trigger is pulled, and the revolver fires!")
            await asyncio.sleep(self.DELAY)
            await msg.edit(
                content=f"The trigger is pulled, and the revolver fires! {ctx.author.mention} lies dead in chat."
            )

            dead = await self.create_dead_role(ctx.guild)
            await ctx.message.author.add_roles(dead)
            await asyncio.sleep(self.reincarnation)
            await ctx.message.author.remove_roles(dead)

        else:
            await msg.edit(content="The trigger is pulled, and the revolver clicks.")
            await asyncio.sleep(self.DELAY)
            await msg.edit(
                content=f"The trigger is pulled, and the revolver clicks. {ctx.author.mention} has lived to survive roulette!"
            )

    async def create_dead_role(self, guild):
        role_name = "Dead Man"
        dead_role = get(guild.roles, name=role_name)

        if not dead_role:
            await guild.create_role(
                name=role_name,
                color=discord.Colour(0x010101),
                reason=f"Created by Kassandra bot. The role is required for {COMMAND_PREFIX}roulette command. Essentially, this role serves the same function as the Muted role",
            )
            dead_role = get(guild.roles, name=role_name)

        for channel in guild.text_channels:
            perm = discord.PermissionOverwrite()
            perm.send_messages = False
            await channel.set_permissions(dead_role, overwrite=perm)

        return dead_role


def setup(bot):
    bot.add_cog(Roulette(bot))
