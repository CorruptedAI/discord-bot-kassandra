import discord
from discord.ext import commands

from modules.time import Time
from modules.postgresql import SELECT
from bot import CHIPS


class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.TWELVE_HOURS = 12 * 60 * 60
        self.time = Time()

    @commands.command()
    @commands.guild_only()
    async def daily(self, ctx):
        user = await self.bot.pg_con.fetchrow(SELECT, ctx.author.id, ctx.guild.id)

        dif = self.time.subtract(user["daily"])

        if dif.total_seconds() >= self.TWELVE_HOURS:
            daily = f"You got 50 {CHIPS}! Come back after 12 hours again for the next reward"
            await self.bot.pg_con.execute(
                """
                UPDATE users
                SET daily = $3, coins = $4
                WHERE user_id = $1 AND guild_id = $2
                """,
                ctx.author.id,
                ctx.guild.id,
                self.time.get_datetime(),
                user["coins"] + 50,
            )
        else:
            daily = self.time.delta(dif)
            daily = f"Not yet! The next reward will be in {daily}"

        await ctx.channel.send(daily)


def setup(bot):
    bot.add_cog(Daily(bot))
