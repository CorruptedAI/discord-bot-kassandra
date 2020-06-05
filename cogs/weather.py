import requests
from datetime import datetime

import discord
from discord.ext import commands

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api = 'http://api.openweathermap.org/data/2.5/weather?appid=6e8d6c451c8bbc61addc2946f4b87ff6&q='

    @commands.command(pass_context=True)
    async def weather(self, ctx, arg=None):
        if not arg:
            return await ctx.channel.send('{0.author.mention}, you forgot to specify the city, try `&weather [city]`'.format(ctx))

        thunder = requests.get(self.api + arg).json()
        embed = discord.Embed(title=thunder['name'],
                              description='**' + thunder['weather'][0]['description'].title() + '**',
                              color=self.bot.user.color)
        embed.set_author(name='Weather', icon_url=self.bot.user.avatar_url)
        embed.add_field(name='Temp',
                        value=str(round(thunder['main']['temp']-273.15, 1)) + '°C',
                        inline=False)
        embed.add_field(name='Feels like',
                        value=str(round(thunder['main']['feels_like']-273.15, 1)) + '°C',
                        inline=False)
        embed.add_field(name='Humidity',
                        value=str(thunder['main']['humidity']) + '%',
                        inline=False)
        embed.add_field(name='Wind',
                        value=str(thunder['wind']['speed']) + ' km/h',
                        inline=False)
        embed.set_footer(text=datetime.now().strftime("%H:%M:%S\n%d.%m.%Y "),
                         icon_url=self.bot.user.avatar_url)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Weather(bot))
