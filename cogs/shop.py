import discord
from discord.ext import commands

from random import randint
import asyncio

from modules.postgresql import SELECT, COINS
from bot import COMMAND_PREFIX, CHIPS, TICKETS


class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.price = {
            "\U0001F516": 50,
            "\U0001F4D7": 150,
            "\U0001F4D8": 400,
            "\U0001F4D5": 1500,
            "\U0001F4D9": 5000,
            "\U0001F4D3": 20000,
            TICKETS: 1,
            "\u2604": 1,
        }

        self.price_symbols = [symbol for symbol in self.price]

    @commands.command()
    @commands.guild_only()
    async def shop(self, ctx):
        user = await self.bot.pg_con.fetchrow(SELECT, ctx.author.id, ctx.guild.id)

        embed = discord.Embed(
            description="**By opening spellbooks, you get experience and tickets!\nBut, you can also buy these items separately if you do not\nwant to try your luck**",
            color=ctx.author.color,
        )

        embed.set_author(name="Shop", icon_url=ctx.author.avatar_url)
        embed.set_footer(
            text=f"BALANCE\n {user['coins']} {CHIPS}", icon_url=self.bot.user.avatar_url
        )

        embed.add_field(
            name=f"{self.price_symbols[0]} Common",
            value=f"{self.price.get(self.price_symbols[0])} {CHIPS}",
            inline=True,
        )
        embed.add_field(
            name=f"{self.price_symbols[1]} Uncommon",
            value=f"{self.price.get(self.price_symbols[1])} {CHIPS}",
            inline=True,
        )
        embed.add_field(
            name=f"{self.price_symbols[2]} Rare",
            value=f"{self.price.get(self.price_symbols[2])} {CHIPS}",
            inline=True,
        )
        embed.add_field(
            name=f"{self.price_symbols[3]} Epic",
            value=f"{self.price.get(self.price_symbols[3])} {CHIPS}",
            inline=True,
        )
        embed.add_field(
            name=f"{self.price_symbols[4]} Legendary",
            value=f"{self.price.get(self.price_symbols[4])} {CHIPS}",
            inline=True,
        )
        embed.add_field(
            name=f"{self.price_symbols[5]} Dark",
            value=f"{self.price.get(self.price_symbols[5])} {CHIPS}",
            inline=True,
        )
        embed.add_field(
            name=f"{self.price_symbols[6]} Ticket",
            value=f"{self.price.get(self.price_symbols[6])} {CHIPS}",
            inline=True,
        )
        embed.add_field(
            name=f"{self.price_symbols[7]} Exp Point",
            value=f"{self.price.get(self.price_symbols[7])} {CHIPS}",
            inline=True,
        )
        msg = await ctx.channel.send(embed=embed)

        await msg.add_reaction(self.price_symbols[0])
        await msg.add_reaction(self.price_symbols[1])
        await msg.add_reaction(self.price_symbols[2])
        await msg.add_reaction(self.price_symbols[3])
        await msg.add_reaction(self.price_symbols[4])
        await msg.add_reaction(self.price_symbols[5])
        await msg.add_reaction(self.price_symbols[6])
        await msg.add_reaction(self.price_symbols[7])

        previous_level = user["level"]
        self.product = ""
        self.q = 0

        def check_reaction(reaction, author):
            if author == ctx.author and str(reaction.message) == str(msg):
                self.product = str(reaction.emoji)
                return True

        def check_quant(q):
            if q.author == ctx.author:
                self.q = q.content
                return True

        try:
            reaction = await self.bot.wait_for(
                "reaction_add", check=check_reaction, timeout=60.0
            )
            await ctx.channel.send(f"How many {self.product} do you want to buy?")
            try:
                reaction = await self.bot.wait_for(
                    "message", check=check_quant, timeout=60.0
                )
                if not self.q.isdigit():
                    return await ctx.channel.send(
                        f":x: You must enter only integer numbers! Enter `{COMMAND_PREFIX}shop` command and try to buy again"
                    )
                self.q = int(self.q)
                self.sum_xp = 0
                self.sum_tick = 0
                if self.product == self.price_symbols[6]:
                    if self.q > user["coins"]:
                        return await ctx.channel.send(
                            f":x: You don't have enough Chips {CHIPS}. Enter `{COMMAND_PREFIX}shop` command and try to buy again. Let me remind you that your balance is indicated at the bottom of the shop, you can also see it using `{COMMAND_PREFIX}balance` and `{COMMAND_PREFIX}profile` commands"
                        )
                    await self.bot.pg_con.execute(
                        """
                        UPDATE users 
                        SET tickets = $3, coins = $4
                        WHERE user_id = $1 AND guild_id = $2
                        """,
                        ctx.author.id,
                        ctx.guild.id,
                        user["tickets"] + self.q,
                        user["coins"] - self.q,
                    )
                    await ctx.channel.send(
                        f"You just bought {self.q} {self.product} for {self.q} {CHIPS}. You now have {user['coins'] - self.q} {CHIPS} left"
                    )
                elif self.product == self.price_symbols[7]:
                    if self.q > user["coins"]:
                        return await ctx.channel.send(
                            f":x: You don't have enough Chips {CHIPS}. Enter `{COMMAND_PREFIX}shop` command and try to buy again. Let me remind you that your balance is indicated at the bottom of the shop, you can also see it using `{COMMAND_PREFIX}balance` and `{COMMAND_PREFIX}profile` commands"
                        )
                    next_level = self.level_up(user["level"], user["exp"] + self.q)
                    await self.bot.pg_con.execute(
                        """
                        UPDATE users 
                        SET exp = $3, coins = $4, level = $5
                        WHERE user_id = $1 AND guild_id = $2
                        """,
                        ctx.author.id,
                        ctx.guild.id,
                        user["exp"] + self.q,
                        user["coins"] - self.q,
                        next_level,
                    )
                    await ctx.channel.send(
                        f"You just bought {self.q} {self.product} for {self.q} {CHIPS}. Now you have {user['coins'] - self.q} {CHIPS} left"
                    )
                    if user["level"] < next_level:
                        await ctx.channel.send(
                            f"{self.price_symbols[7]} Congrats! Your level is up from {user['level']} to {next_level}"
                        )
                else:
                    total = self.q * self.price.get(self.product)
                    if total > user["coins"]:
                        return await ctx.channel.send(
                            f":x: You don't have enough Chips {CHIPS}. Enter `{COMMAND_PREFIX}shop` command and try to buy again. Let me remind you that your balance is indicated at the bottom of the shop, you can also see it using `{COMMAND_PREFIX}balance` and `{COMMAND_PREFIX}profile` commands"
                        )
                    self.xp, self.tick = [0, 0]
                    i = self.q
                    while i > 0:
                        self.xp, self.tick = self.check_price()
                        self.sum_xp += self.xp
                        self.sum_tick += self.tick
                        i -= 1
                    next_level = self.level_up(user["level"], user["exp"] + self.sum_xp)
                    await self.bot.pg_con.execute(
                        """
                        UPDATE users 
                        SET exp = $3, tickets = $4, coins = $5, level = $6
                        WHERE user_id = $1 AND guild_id = $2
                        """,
                        ctx.author.id,
                        ctx.guild.id,
                        user["exp"] + self.sum_xp,
                        user["tickets"] + self.sum_tick,
                        user["coins"] - total,
                        next_level,
                    )
                    await ctx.channel.send(
                        f"By opening {self.q} {self.product} you have recieved {self.sum_xp} {self.price_symbols[7]} and {self.sum_tick} {self.price_symbols[6]}. Now you have {user['coins'] - total} {CHIPS}"
                    )
                    if user["level"] < next_level:
                        await ctx.channel.send(
                            f"{self.price_symbols[7]} Congrats! Your level is up from {user['level']} to {next_level}"
                        )

            except asyncio.TimeoutError:
                return
        except asyncio.TimeoutError:
            return

    def level_up(self, level, exp):
        up = self.pokemon_generation(level)
        while up <= exp:
            level += 1
            up = self.pokemon_generation(level)
        return level - 1

    def pokemon_generation(self, level):
        return round((4 * (level ** 3)) / 5) * 10

    def check_price(self):
        if self.product == self.price_symbols[0]:
            return randint(20, 80), randint(2, 8)
        elif self.product == self.price_symbols[1]:
            return randint(100, 200), randint(10, 20)
        elif self.product == self.price_symbols[2]:
            return randint(300, 500), randint(30, 50)
        elif self.product == self.price_symbols[3]:
            return randint(1000, 2000), randint(100, 200)
        elif self.product == self.price_symbols[4]:
            return randint(2000, 8000), randint(200, 800)
        elif self.product == self.price_symbols[5]:
            return randint(0, 50000), randint(0, 2000)


def setup(bot):
    bot.add_cog(Shop(bot))
