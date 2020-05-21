﻿import random
import asyncio

import discord
from discord.ext import commands

class Slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.symbols_dict = {
                   '\U0001F34A': [0.5, 1.5,  3.5],      # :tangerine:
                   '\U0001F347': [0.5, 1.5,  4.0],      # :grapes:
                   '\U0001F352': [0.5, 2.0,  5.0],      # :cherries:
                   '\U0001F34B': [0.5, 2.5,  6.5],      # :lemon:
                   '\U0001F349': [1.5, 5.0,  20.0],     # :watermelon:
                   '\U0001F95D': [2.0, 8.0,  35.0],     # :kiwi:
                   '\U0001F353': [3.0, 15.0, 60.0],     # :strawberry:
                   '\U0001F351': [4.0, 25.0, 80.0],     # :peach:
                   '\U0001F48E': [0]         # wild     # :gem:         
                   }

        self.symbols = []
        for symbol in self.symbols_dict:
            self.symbols.append(symbol)

        self.SPIN = '\U0001F1F8'
        self.COOKIE = ' \U0001F36A'

    @commands.command(pass_context=True)
    async def slots(self, ctx, arg='help'):
        if arg == 'help':
            return await ctx.channel.send('help slots testing')
        else:
            self.bet_value = int(arg)
        self.balance_value = str(0) # get balance

        self.lines = self.generate_line() + self.generate_line() + self.generate_line()
        self.embed = self.update_ui(ctx, True)
        self.msg = await ctx.channel.send(embed=self.embed)
        await self.msg.add_reaction(self.SPIN)
        await self.msg.edit(embed=self.embed)

        def check_reaction(reaction, user):
            return user == ctx.author and str(reaction.emoji) == self.SPIN

        while True:
            try:
                reaction = await self.bot.wait_for('reaction_add', check=check_reaction, timeout=90.0)
            except asyncio.TimeoutError:
                return 

            if reaction:
                self.DELAY = .2
                for i in range(3):
                    self.lines = self.generate_sequence()
                    self.embed = self.update_ui(ctx)
                    await self.msg.edit(embed=self.embed)
                    self.DELAY += self.DELAY/10
                    await asyncio.sleep(self.DELAY)
                self.embed = self.update_ui(ctx, False, True)
                await self.msg.edit(embed=self.embed)
                await self.msg.remove_reaction(self.SPIN, ctx.author)

    def update_ui(self, ctx_m, opening=False, ending=False):
        space = '\n** ** '
        embed = discord.Embed(title=self.show_reels(),
                              color=ctx_m.author.color)
        embed.set_author(name='Slots',
                         icon_url=ctx_m.author.avatar_url)
        embed.add_field(name='**BET**',
                        value=self.bet_value,
                        inline=True)
        embed.add_field(name='**BALANCE**',
                        value=self.balance_value,
                        inline=True)
        if opening:
            embed.set_footer(text='Press S\nto spin',
                             icon_url=self.bot.user.avatar_url)
        else:
            if ending:
                embed.set_footer(text='WIN\n ' + str(round(self.bet_value*self.get_multiplier())) + self.COOKIE,
                                 icon_url=self.bot.user.avatar_url)
            else:
                embed.set_footer(text='WIN\n 0' + self.COOKIE,
                                 icon_url=self.bot.user.avatar_url)
        return embed

    def generate_line(self):
        line = []
        for i in range(5):
            line.append(random.choice(self.symbols))
        return line

    def show_reels(self):
        space = '\n** ** '
        beauty_lines = ''

        for i in range(15):
            if i % 5 == 0:
                beauty_lines += space
            beauty_lines += self.lines[i]

        return beauty_lines

    def generate_sequence(self):
        del self.lines[10:15]
        return self.generate_line() + self.lines

    def check_line(self, reel1, reel2, reel3, reel4, reel5):
        result = 0
        symbol_main = ''
        lines_copy = self.lines.copy()
        wild_score = 0
        wild_symbol = ''

        for n in [reel1, reel2, reel3, reel4, reel5]:
            if self.lines[n] != self.symbols[8]:
                symbol_main = n
                wild_symbol = self.lines[n]
                break

        for n in [reel1, reel2, reel3, reel4, reel5]:
            if self.lines[n] == self.symbols[8]:
                #wild_score += 5
                self.lines[n] = wild_symbol

        if self.lines[reel1] == self.lines[reel2] == self.lines[reel3]:
            if self.lines[reel3] == self.lines[reel4]:
                if self.lines[reel4] == self.lines[reel5]:
                    result += self.symbols_dict.get(self.lines[symbol_main])[2]
                else:
                    result += self.symbols_dict.get(self.lines[symbol_main])[1]
            else:
                result += self.symbols_dict.get(self.lines[symbol_main])[0]

        self.lines = lines_copy

        return result + wild_score
    
    def get_multiplier(self):
        result = self.check_line(0, 1, 2, 3, 4)
        result += self.check_line(0, 6, 12, 8, 4)
        result += self.check_line(0, 6, 7, 8, 4)
        result += self.check_line(0, 1, 7, 3, 4)
        result += self.check_line(0, 6, 2, 8, 4)
        result += self.check_line(0, 11, 12, 13, 4)

        result += self.check_line(5, 6, 7, 8, 9)
        result += self.check_line(5, 2, 3, 8, 9)
        result += self.check_line(5, 1, 2, 3, 9)
        result += self.check_line(5, 11, 12, 13, 9)
        result += self.check_line(5, 6, 2, 8, 9)
        result += self.check_line(5, 6, 12, 8, 9)
        result += self.check_line(5, 1, 7, 3, 9)
        result += self.check_line(5, 11, 7, 13, 9)

        result += self.check_line(10, 11, 12, 13, 14)
        result += self.check_line(10, 6, 2, 8, 14)
        result += self.check_line(10, 6, 7, 8, 14)
        result += self.check_line(10, 11, 7, 13, 14)
        result += self.check_line(10, 6, 12, 8, 14)
        result += self.check_line(10, 1, 2, 3, 14)
        result += self.check_line(10, 11, 2, 13, 14)

        return result

def setup(bot):
    bot.add_cog(Slots(bot))