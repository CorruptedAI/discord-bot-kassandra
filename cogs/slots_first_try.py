import random
import asyncio

import discord
from discord.ext import commands

class Slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.symbols = [
                   ':tangerine:',
                   ':grapes:',
                   ':cherries:',
                   ':lemon:',
                   ':watermelon:',
                   ':kiwi:',
                   ':strawberry:',
                   ':peach:',
                   ':gem:']

        self.SPIN = '\U0001F1F8'

    @commands.command()
    async def slots(self, ctx):
        self.lines = self.generate_three_lines()
        self.embed = self.update_ui(ctx, self.lines, '4', '3', '0', True)
        self.msg = await ctx.channel.send(embed=self.embed)
        await self.msg.add_reaction(self.SPIN)
        await self.msg.edit(embed=self.embed)

        def check_reaction(reaction, user):
            return user == ctx.author and str(reaction.emoji) == self.SPIN

        while True:
            try:
                reaction = await self.bot.wait_for('reaction_add', check=check_reaction, timeout=60.0)
            except asyncio.TimeoutError:
                return await ctx.channel.send('You took too long, {0.author.mention}. Your frame was closed.'.format(ctx))

            if reaction:
                self.DELAY = .3
                i = 0
                while i < 5:
                    self.lines = self.generate_animation(self.lines)
                    self.embed = self.update_ui(ctx, self.lines, '4', '3', '0')
                    await self.msg.edit(embed=self.embed)
                    self.DELAY += self.DELAY/10
                    await asyncio.sleep(self.DELAY)
                    i += 1
                self.embed = self.update_ui(ctx, self.lines, '4', '3', str(self.check_line1(self.lines) + self.check_line2(self.lines) + self.check_line3(self.lines)))
                await self.msg.edit(embed=self.embed)

                await self.msg.remove_reaction(self.SPIN, ctx.author)

    def set_multiplier(self, symbol):
        n3 = n4 = n5 = 0

        if symbol == self.symbols[0]:
            n3 = 1
            n4 = 3
            n5 = 7

        elif symbol == self.symbols[1]:
            n3 = 1
            n4 = 3
            n5 = 8

        elif symbol == self.symbols[2]:
            n3 = 1
            n4 = 4
            n5 = 10

        elif symbol == self.symbols[3]:
            n3 = 1
            n4 = 5
            n5 = 13

        elif symbol == self.symbols[4]:
            n3 = 3
            n4 = 10
            n5 = 40

        elif symbol == self.symbols[5]:
            n3 = 4
            n4 = 16
            n5 = 70

        elif symbol == self.symbols[6]:
            n3 = 6
            n4 = 30
            n5 = 120

        elif symbol == self.symbols[7]:
            n3 = 8
            n4 = 50
            n5 = 160

        elif symbol == self.symbols[8]:
            n3 = 20
            n4 = 100
            n5 = 370

        return [n3, n4, n5]

    def check_line1(self, lines):
        result = 0

        temp_list = self.set_multiplier(lines[0])
        n3 = temp_list[0]
        n4 = temp_list[1]
        n5 = temp_list[2]

        if lines[0] == lines[1] == lines[2]:
             if lines[2] == lines[3]:
                 if lines[3] == lines[4]:
                     result += n5
                 else:
                     result += n4
             else:
                 result += n3
        else:
             result += 0

        return result

    def check_line2(self, lines):
        result = 0

        temp_list = self.set_multiplier(lines[5])
        n3 = temp_list[0]
        n4 = temp_list[1]
        n5 = temp_list[2]

        if lines[5] == lines[6]:
            if lines[6] == lines[7]:
                if lines[7] == lines[8]:
                    if lines[8] == lines[9]:
                        result += n5
                    else:
                        result += n4
                else:
                    result += n3
            else:
                result += 0
        else:
            result += 0

        return result

    def check_line3(self, lines):
        result = 0

        temp_list = self.set_multiplier(lines[10])
        n3 = temp_list[0]
        n4 = temp_list[1]
        n5 = temp_list[2]

        if lines[10] == lines[11]:
            if lines[11] == lines[12]:
                if lines[13] == lines[14]:
                    if lines[14] == lines[15]:
                        result += n5
                    else:
                        result += n4
                else:
                    result += n3
            else:
                result += 0
        else:
            result += 0

        return result


    def generate_animation(self, lines):
        del lines[10:15]
        return self.generate_line() + lines

    def update_ui(self, ctx_m, lines, bet_value, balance_value, win_value, starting=False):
        space = '\n** ** '
        embed = discord.Embed(title=space+lines[0]+lines[1]+lines[2]+lines[3]+lines[4]+
                                    space+lines[5]+lines[6]+lines[7]+lines[8]+lines[9]+
                                    space+lines[10]+lines[11]+lines[12]+lines[13]+lines[14]
                              , color=ctx_m.author.color)
        embed.set_author(name='Slots',
                         icon_url=ctx_m.author.avatar_url)
        embed.add_field(name='**BET**',
                        value=bet_value,
                        inline=True)
        embed.add_field(name='**BALANCE**',
                        value=balance_value,
                        inline=True)
        if starting:
            embed.set_footer(text='Press S\nto spin',
                            icon_url=self.bot.user.avatar_url)
        else:
            embed.set_footer(text='WIN\n ' + win_value,
                            icon_url=self.bot.user.avatar_url)
        return embed

    def generate_line(self):
        i = 0
        line = []
        while i < 5:
            line.append(random.choice(self.symbols))
            i += 1
        return line

    def generate_three_lines(self, beautifier=False):
        return (self.generate_line() + self.generate_line() + self.generate_line())

    def calculate_multiplier(self, lines):
        pass

def setup(bot):
    bot.add_cog(Slots(bot))
