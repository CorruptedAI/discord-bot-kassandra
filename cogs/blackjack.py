import discord
from discord.ext import commands

import random
import asyncio

from modules.postgresql import SELECT, COINS
from bot import COMMAND_PREFIX, CHIPS


class Blackjack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.DELAY = 0.8

        self.deck_list = {
            "2♣": 2,   "2♦":  2,  "2♥":  2,  "2♠": 2,
            "3♣": 3,   "3♦":  3,  "3♥":  3,  "3♠": 3,
            "4♣": 4,   "4♦":  4,  "4♥":  4,  "4♠": 4,
            "5♣": 5,   "5♦":  5,  "5♥":  5,  "5♠": 5,
            "6♣": 6,   "6♦":  6,  "6♥":  6,  "6♠": 6,
            "7♣": 7,   "7♦":  7,  "7♥":  7,  "7♠": 7,
            "8♣": 8,   "8♦":  8,  "8♥":  8,  "8♠": 8,
            "9♣": 9,   "9♦":  9,  "9♥":  9,  "9♠": 9,
            "10♣": 10, "10♦": 10, "10♥": 10, "10♠": 10,
            "J♣": 10,  "J♦":  10, "J♥":  10, "J♠": 10,
            "Q♣": 10,  "Q♦":  10, "Q♥":  10, "Q♠": 10,
            "K♣": 10,  "K♦":  10, "K♥":  10, "K♠": 10,
            "A♣": 11,  "A♦":  11, "A♥":  11, "A♠": 11,
        }

        self.HIT = "\U0001F1ED"
        self.STAND = "\U0001F1F8"

    @commands.command(aliases=["bj"])
    @commands.guild_only()
    @commands.bot_has_permissions(manage_emojis=True, manage_messages=True)
    async def blackjack(self, ctx, bet=None):
        if not bet:
            return await ctx.channel.send(
                f":x: You must enter your bet! Enter `{COMMAND_PREFIX}blackjack [bet]` command and try to play again"
            )

        if not bet.isdigit():
            return await ctx.channel.send(
                f":x: A bet can only be an integer! Enter `{COMMAND_PREFIX}blackjack [bet]` command and try to play again"
            )

        self.bet = int(bet)
        self.author_id = ctx.author.id
        self.guild_id = ctx.guild.id

        self.user = await self.bot.pg_con.fetchrow(
            SELECT, self.author_id, self.guild_id
        )

        if self.bet > self.user["coins"]:
            return await ctx.channel.send(
                f":x: Not enough chips. Your balance is {user['coins']} {CHIPS}. Try to enter a different amount or enter `{COMMAND_PREFIX}daily` command to get a daily reward"
            )

        await self.bot.pg_con.execute(
            COINS, self.author_id, self.guild_id, self.user["coins"] - self.bet
        )

        self.player = []
        self.dealer = []

        self.deck = [card for card in self.deck_list]

        # Game setup
        self.setup_turn()
        self.embed = self.update_ui(ctx)
        self.stop_flag = False
        await self.check_blackjack(ctx)
        self.msg = await ctx.channel.send(embed=self.embed)
        await self.msg.edit(embed=self.embed)

        await self.msg.add_reaction(self.HIT)
        await self.msg.add_reaction(self.STAND)

        self.hit_clicked = False
        self.stand_clicked = False

        def check_reaction(reaction, user):
            if str(reaction.emoji) == self.HIT:
                self.hit_clicked = True
                return user == ctx.author and str(reaction.message) == str(self.msg)
            elif str(reaction.emoji) == self.STAND:
                self.stand_clicked = True
                return user == ctx.author and str(reaction.message) == str(self.msg)

        # Game loop
        while True:
            if self.stop_flag:
                break

            try:
                reaction = await self.bot.wait_for(
                    "reaction_add", check=check_reaction, timeout=60.0
                )
            except asyncio.TimeoutError:
                reaction = self.stand_clicked = True
                await ctx.channel.send(
                    f":x: {ctx.author.mention} you took too long, your game has been closed, to start over, enter `{COMMAND_PREFIX}blackjack` command"
                )

            if reaction and self.hit_clicked:
                self.hit_clicked = False

                self.get_card(self.player)
                self.embed = self.update_ui(ctx)
                await self.msg.edit(embed=self.embed)

                if self.check_edge(self.player):
                    self.embed = self.update_ui(ctx, "BUST", True)
                    await self.msg.edit(embed=self.embed)
                    break

                await self.msg.remove_reaction(self.HIT, ctx.author)

            elif reaction and self.stand_clicked:
                self.stand_clicked = False

                self.embed = self.update_ui(ctx, "Dealer's hand", True)
                await self.msg.edit(embed=self.embed)
                await asyncio.sleep(self.DELAY)

                while self.get_score(self.dealer) < 17:
                    self.get_card(self.dealer)
                    self.embed = self.update_ui(ctx, "Drawing...", True)
                    await self.msg.edit(embed=self.embed)
                    await asyncio.sleep(self.DELAY)

                if self.check_edge(self.dealer):
                    await self.bot.pg_con.execute(
                        COINS,
                        self.author_id,
                        self.guild_id,
                        self.user["coins"] + self.bet * 2,
                    )
                    self.embed = self.update_ui(ctx, "WIN", True)
                    await self.msg.edit(embed=self.embed)
                    break

                self.embed = self.update_ui(ctx, await self.check_result(), True)
                await self.msg.edit(embed=self.embed)
                break

    def get_card(self, user):
        card = random.choice(self.deck)
        user.append(card)
        self.deck.remove(card)
        return card

    def get_score(self, user, ra9=True):
        if not ra9:
            return str(self.deck_list.get(user[0]))

        deck_score = []
        for n in user:
            deck_score.append(self.deck_list.get(n))

        if sum(deck_score) > 21:
            for i, n in enumerate(deck_score):
                if deck_score[i] == 11:
                    deck_score[i] = 1

        return sum(deck_score)

    def show_cards(self, user, ra9=True):
        if ra9:
            return " ".join("`" + item + "`" for item in user)
        return "`" + user[0] + "` `?`"

    def update_ui(self, ctx_m, footer_m="Would you like\nto stand on it?", ra9=False):
        embed = discord.Embed(color=ctx_m.author.color)
        embed.set_author(name="Blackjack", icon_url=ctx_m.author.avatar_url)
        embed.set_footer(text=footer_m, icon_url=self.bot.user.avatar_url)
        embed.add_field(
            name=f"Your score: **{self.get_score(self.player)}**",
            value=self.show_cards(self.player),
            inline=False,
        )
        embed.add_field(
            name=f"Dealer score: **{self.get_score(self.dealer, ra9)}**",
            value=self.show_cards(self.dealer, ra9),
            inline=False,
        )
        return embed

    def setup_turn(self):
        self.get_card(self.player)
        self.get_card(self.dealer)
        self.get_card(self.player)
        self.get_card(self.dealer)

    def check_edge(self, user):
        if self.get_score(user) > 21:
            return True
        return False

    async def check_result(self):
        if (
            self.get_score(self.player) > self.get_score(self.dealer)
        ) and not self.check_edge(self.player):
            await self.bot.pg_con.execute(
                COINS, self.author_id, self.guild_id, self.user["coins"] + self.bet * 2
            )
            return "WIN"
        elif self.get_score(self.player) == self.get_score(self.dealer):
            await self.bot.pg_con.execute(
                COINS, self.author_id, self.guild_id, self.user["coins"]
            )
            return "PUSH"
        else:
            return "LOSE"

    async def check_blackjack(self, ctx_m):
        if self.get_score(self.player, True) == 21:
            if self.get_score(self.dealer, True) == 21:
                await self.bot.pg_con.execute(
                    COINS, self.author_id, self.guild_id, self.user["coins"]
                )
                self.embed = self.update_ui(ctx_m, "BLACKJACK\n PUSH", True)
                self.stop_flag = True
            else:
                await self.bot.pg_con.execute(
                    COINS,
                    self.author_id,
                    self.guild_id,
                    self.user["coins"] + self.bet * 2.5,
                )
                self.embed = self.update_ui(ctx_m, "BLACKJACK\n WIN", True)
                self.stop_flag = True
        elif self.get_score(self.dealer, True) == 21:
            self.embed = self.update_ui(ctx_m, "BLACKJACK\n LOSE", True)
            self.stop_flag = True


def setup(bot):
    bot.add_cog(Blackjack(bot))
