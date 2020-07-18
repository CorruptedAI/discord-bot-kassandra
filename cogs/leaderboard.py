import discord
from discord.ext import commands


class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def leaderboard(self, ctx, mode: str = "local"):
        embed = discord.Embed(color=self.bot.user.color)
        embed.set_author(name="Kassandra", icon_url=self.bot.user.avatar_url)

        if mode != "global":
            embed.title = ":fog: Local Leaderboard"
            top = await self.bot.pg_con.fetch(
                """
                SELECT *
                FROM users
                ORDER BY level DESC
                LIMIT 5
                """
            )
            pos = 1
            for user in top:
                if user["guild_id"] == ctx.guild.id:
                    user_info = self.bot.get_user(user["user_id"])
                    embed.add_field(
                        name=f"{pos}. {user_info}",
                        value=f":comet: **{user['level']}** [{user['exp']}]",
                        inline=False,
                    )
                    pos += 1

        else:
            embed.title = ":map: Global Leaderboard"
            top = await self.bot.pg_con.fetch(
                """
                SELECT *
                FROM users
                ORDER BY level DESC
                LIMIT 5
                """
            )
            pos = 1
            for user in top:
                user_info = self.bot.get_user(user["user_id"])
                embed.add_field(
                    name=f"{pos}. {user_info}",
                    value=f":comet: **{user['level']}** [{user['exp']}]",
                    inline=False,
                )
                pos += 1

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Leaderboard(bot))
