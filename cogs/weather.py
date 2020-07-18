import discord
from discord.ext import commands

from settings import load_openweather_token
from modules.openweather import OpenWeather
from modules.time import Time
from bot import COMMAND_PREFIX


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.current_time = Time()

    @commands.command()
    async def weather(self, ctx, city=None):
        if not city:
            return await ctx.channel.send(
                f":x: You must specify a city, for example`{COMMAND_PREFIX}weather Prague`"
            )

        current_forecast = OpenWeather(load_openweather_token(), city)
        if current_forecast.get_error():
            return await ctx.channel.send(
                f":x: Unfortunately, I could not find **{city}**, make sure you entered the city correctly"
            )

        embed = discord.Embed(
            title=current_forecast.get_name(),
            description=f"**{current_forecast.get_description().title()}**",
            color=self.bot.user.color,
        )
        embed.add_field(
            name="Temperature",
            value=f"{round(current_forecast.get_temp('c'), 1)} °C",
            inline=True,
        )
        embed.add_field(
            name="Temperature",
            value=f"{round(current_forecast.get_temp('f'), 1)} °F",
            inline=True,
        )
        embed.add_field(
            name="Humidity", value=f"{current_forecast.get_humidity()} %", inline=False
        )
        embed.add_field(
            name="Cloudiness", value=f"{current_forecast.get_clouds()} %", inline=False
        )
        embed.add_field(
            name="Wind",
            value=f"{current_forecast.get_wind_speed('k')} km/h",
            inline=False,
        )
        embed.set_footer(
            # text=f"{self.current_time.get_short_time()}\n{self.current_time.get_date()}",
            text=self.current_time.get_date(),
            icon_url=self.bot.user.avatar_url,
        )

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Weather(bot))
